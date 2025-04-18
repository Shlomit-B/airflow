#
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
"""Example DAG demonstrating the usage of the JdbcOperator."""

from __future__ import annotations

import os
from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.providers.standard.operators.empty import EmptyOperator

ENV_ID = os.environ.get("SYSTEM_TESTS_ENV_ID")
DAG_ID = "example_jdbc_operator"

with DAG(
    dag_id=DAG_ID,
    schedule="0 0 * * *",
    start_date=datetime(2021, 1, 1),
    dagrun_timeout=timedelta(minutes=60),
    tags=["example"],
    catchup=False,
) as dag:
    run_this_last = EmptyOperator(task_id="run_this_last")

    # [START howto_operator_jdbc_template]
    delete_data = SQLExecuteQueryOperator(
        task_id="delete_data",
        sql="delete from my_schema.my_table where dt = {{ ds }}",
        conn_id="my_jdbc_connection",
        autocommit=True,
    )
    # [END howto_operator_jdbc_template]

    # [START howto_operator_jdbc]
    insert_data = SQLExecuteQueryOperator(
        task_id="insert_data",
        sql="insert into my_schema.my_table select dt, value from my_schema.source_data",
        conn_id="my_jdbc_connection",
        autocommit=True,
    )
    # [END howto_operator_jdbc]

    delete_data >> insert_data >> run_this_last

    from tests_common.test_utils.watcher import watcher

    # This test needs watcher in order to properly mark success/failure
    # when "tearDown" task with trigger rule is part of the DAG
    list(dag.tasks) >> watcher()

from tests_common.test_utils.system_tests import get_test_run  # noqa: E402

# Needed to run the example DAG with pytest (see: tests/system/README.md#run_via_pytest)
test_run = get_test_run(dag)
