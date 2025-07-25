# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from __future__ import annotations

import os
from datetime import datetime

from airflow import DAG

try:
    from airflow.sdk import task, teardown
except ImportError:
    # Airflow 2 path
    from airflow.decorators import task, teardown  # type: ignore[attr-defined,no-redef]
from airflow.providers.pinecone.operators.pinecone import CreatePodIndexOperator

index_name = os.getenv("INDEX_NAME", "test")


with DAG(
    "example_pinecone_create_pod_index",
    schedule="@once",
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:
    # [START howto_operator_create_pod_index]
    # reference: https://docs.pinecone.io/reference/api/control-plane/create_index
    create_index = CreatePodIndexOperator(
        task_id="pinecone_create_pod_index",
        index_name=index_name,
        dimension=3,
        replicas=1,
        shards=1,
        pods=1,
        pod_type="p1.x1",
    )
    # [END howto_operator_create_pod_index]

    @teardown
    @task
    def delete_index():
        from airflow.providers.pinecone.hooks.pinecone import PineconeHook

        hook = PineconeHook()
        hook.delete_index(index_name=index_name)

    create_index >> delete_index()


from tests_common.test_utils.system_tests import get_test_run  # noqa: E402

# Needed to run the example DAG with pytest (see: tests/system/README.md#run_via_pytest)
test_run = get_test_run(dag)
