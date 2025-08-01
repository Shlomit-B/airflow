 .. Licensed to the Apache Software Foundation (ASF) under one
    or more contributor license agreements.  See the NOTICE file
    distributed with this work for additional information
    regarding copyright ownership.  The ASF licenses this file
    to you under the Apache License, Version 2.0 (the
    "License"); you may not use this file except in compliance
    with the License.  You may obtain a copy of the License at

 ..   http://www.apache.org/licenses/LICENSE-2.0

 .. Unless required by applicable law or agreed to in writing,
    software distributed under the License is distributed on an
    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.

Static code checks
==================

The static code checks in Airflow are used to verify that the code meets certain quality standards.
All the static code checks can be run through pre-commit hooks.

The pre-commit hooks perform all the necessary installation when you run them
for the first time. See the table below to identify which pre-commit checks require the Breeze Docker images.

You can also run the checks via `Breeze <../dev/breeze/doc/README.rst>`_ environment.

**The outline for this document in GitHub is available at top-right corner button (with 3-dots and 3 lines).**

Pre-commit hooks
----------------

Pre-commit hooks help speed up your local development cycle and place less burden on the CI infrastructure.
Consider installing the pre-commit hooks as a necessary prerequisite.

The pre-commit hooks by default only check the files you are currently working on and make
them fast. Yet, these checks use exactly the same environment as the CI tests
use. So, you can be sure your modifications will also work for CI if they pass
pre-commit hooks.

We have integrated the fantastic `pre-commit <https://pre-commit.com>`__ framework
in our development workflow. To install and use it, you need at least Python 3.10 locally.

Installing pre-commit hooks
---------------------------

It is the best to use pre-commit hooks when you have your local virtualenv for
Airflow activated since then pre-commit hooks and other dependencies are
automatically installed. You can also install the pre-commit hooks manually using ``uv`` or ``pip``.

.. code-block:: bash

    uv tool install pre-commit

.. code-block:: bash

    pip install pre-commit

After installation, pre-commit hooks are run automatically when you commit the code and they will
only run on the files that you change during your commit, so they are usually pretty fast and do
not slow down your iteration speed on your changes. There are also ways to disable the ``pre-commits``
temporarily when you commit your code with ``--no-verify`` switch or skip certain checks that you find
to much disturbing your local workflow. See `Available pre-commit checks <#available-pre-commit-checks>`_
and `Using pre-commit <#using-pre-commit>`_

The pre-commit hooks use several external linters that need to be installed before pre-commit is run.
Each of the checks installs its own environment, so you do not need to install those, but there are some
checks that require locally installed binaries. On Linux, you typically install
them with ``sudo apt install``, on macOS - with ``brew install``.

The current list of prerequisites is limited to ``xmllint``:

- on Linux, install via ``sudo apt install libxml2-utils``
- on macOS, install via ``brew install libxml2``

Some pre-commit hooks also require the Docker Engine to be configured as the static
checks are executed in the Docker environment (See table in the
`Available pre-commit checks <#available-pre-commit-checks>`_ . You should build the images
locally before installing pre-commit checks as described in `Breeze docs <../dev/breeze/doc/README.rst>`__.

Sometimes your image is outdated and needs to be rebuilt because some dependencies have been changed.
In such cases, the Docker-based pre-commit will inform you that you should rebuild the image.

In case you do not have your local images built, the pre-commit hooks fail and provide
instructions on what needs to be done.

Enabling pre-commit hooks
-------------------------

To turn on pre-commit checks for ``commit`` operations in git, enter:

.. code-block:: bash

    pre-commit install


To install the checks also for ``pre-push`` operations, enter:

.. code-block:: bash

    pre-commit install -t pre-push


For details on advanced usage of the install method, use:

.. code-block:: bash

   pre-commit install --help

Available pre-commit checks
---------------------------

This table lists pre-commit hooks used by Airflow. The ``Image`` column indicates which hooks
require Breeze Docker image to be built locally.

  .. BEGIN AUTO-GENERATED STATIC CHECK LIST

+-----------------------------------------------------------+--------------------------------------------------------+---------+
| ID                                                        | Description                                            | Image   |
+===========================================================+========================================================+=========+
| bandit                                                    | bandit                                                 |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| blacken-docs                                              | Run black on docs                                      |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-aiobotocore-optional                                | Check if aiobotocore is an optional dependency only    |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-airflow-k8s-not-used                                | Check airflow.kubernetes imports are not used          |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-airflow-providers-bug-report-template               | Sort airflow-bug-report provider list                  |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-airflow-v-imports-in-tests                          | Check AIRFLOW_V imports in tests                       |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-apache-license-rat                                  | Check if licenses are OK for Apache                    |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-base-operator-partial-arguments                     | Check BaseOperator and partial() arguments             |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-base-operator-usage                                 | * Check BaseOperator core imports                      |         |
|                                                           | * Check BaseOperatorLink core imports                  |         |
|                                                           | * Check BaseOperator other imports                     |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-boring-cyborg-configuration                         | Checks for Boring Cyborg configuration consistency     |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-breeze-top-dependencies-limited                     | Check top-level breeze deps                            |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-builtin-literals                                    | Require literal syntax when initializing builtins      |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-changelog-format                                    | Check changelog format                                 |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-changelog-has-no-duplicates                         | Check changelogs for duplicate entries                 |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-cncf-k8s-only-for-executors                         | Check cncf.kubernetes imports used for executors only  |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-code-deprecations                                   | Check deprecations categories in decorators            |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-common-compat-used-for-openlineage                  | Check common.compat is used for OL deprecated classes  |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-core-deprecation-classes                            | Verify usage of Airflow deprecation classes in core    |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-decorated-operator-implements-custom-name           | Check @task decorator implements custom_operator_name  |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-default-configuration                               | Check the default configuration                        | *       |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-deferrable-default                                  | Check and fix default value of default_deferrable      |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-docstring-param-types                               | Check that docstrings do not specify param types       |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-example-dags-urls                                   | Check that example dags url include provider versions  |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-executables-have-shebangs                           | Check that executables have shebang                    |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-extra-packages-references                           | Checks setup extra packages                            |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-extras-order                                        | Check order of extras in Dockerfile                    |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-fab-migrations                                      | Check no migration is done on FAB related table        |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-for-inclusive-language                              | Check for language that we do not accept as community  |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-get-lineage-collector-providers                     | Check providers import hook lineage code from compat   |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-hooks-apply                                         | Check if all hooks apply to the repository             |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-i18n-json                                           | Check i18n files validity                              | *       |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-imports-in-providers                                | Check imports in providers                             | *       |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-incorrect-use-of-LoggingMixin                       | Make sure LoggingMixin is not used alone               |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-init-decorator-arguments                            | Sync model __init__ and decorator arguments            |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-integrations-list-consistent                        | Sync integrations list with docs                       |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-lazy-logging                                        | Check that all logging methods are lazy                |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-links-to-example-dags-do-not-use-hardcoded-versions | Verify no hard-coded version in example dags           |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-merge-conflict                                      | Check that merge conflicts are not being committed     |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-min-python-version                                  | Check minimum Python version                           |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-newsfragments-are-valid                             | Check newsfragments are valid                          |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-no-airflow-deprecation-in-providers                 | Do not use DeprecationWarning in providers             |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-no-providers-in-core-examples                       | No providers imports in core example DAGs              |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-only-new-session-with-provide-session               | Check NEW_SESSION is only used with @provide_session   |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-persist-credentials-disabled-in-github-workflows    | Check persistent creds in workflow files               |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-pre-commit-information-consistent                   | Validate hook IDs & names and sync with docs           |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-provide-create-sessions-imports                     | Check session util imports                             |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-provider-docs-valid                                 | Validate provider doc files                            |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-provider-yaml-valid                                 | Validate provider.yaml files                           | *       |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-providers-subpackages-init-file-exist               | Provider subpackage init files are there               |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-pydevd-left-in-code                                 | Check for pydevd debug statements accidentally left    |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-pytest-mark-db-test-in-providers                    | Check pytest.mark.db_test use in providers             |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-revision-heads-map                                  | Check that the REVISION_HEADS_MAP is up-to-date        |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-safe-filter-usage-in-html                           | Don't use safe in templates                            |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-sdk-imports                                         | Check for SDK imports in core files                    | *       |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-significant-newsfragments-are-valid                 | Check significant newsfragments are valid              |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-sql-dependency-common-data-structure                | Check dependency of SQL providers                      |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-start-date-not-used-in-defaults                     | start_date not in default_args                         |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-system-tests-present                                | Check if system tests have required segments of code   |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-system-tests-tocs                                   | Check that system tests is properly added              |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-taskinstance-tis-attrs                              | Check that TI and TIS have the same attributes         |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-template-context-variable-in-sync                   | Sync template context variable refs                    |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-template-fields-valid                               | Check templated fields mapped in operators/sensors     | *       |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-tests-in-the-right-folders                          | Check if tests are in the right folders                |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-tests-unittest-testcase                             | Unit tests do not inherit from unittest.TestCase       |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-urlparse-usage-in-code                              | Don't use urlparse in code                             |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-xml                                                 | Check XML files with xmllint                           |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| check-zip-file-is-not-committed                           | Check no zip files are committed                       |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| codespell                                                 | Run codespell                                          |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| compile-fab-assets                                        | Compile FAB provider assets                            |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| compile-ui-assets                                         | Compile ui assets (manual)                             |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| compile-ui-assets-dev                                     | Compile ui assets in dev mode (manual)                 |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| create-missing-init-py-files-tests                        | Create missing init.py files in tests                  |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| debug-statements                                          | Detect accidentally committed debug statements         |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| detect-private-key                                        | Detect if private key is added to the repository       |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| doctoc                                                    | Add TOC for Markdown and RST files                     |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| end-of-file-fixer                                         | Make sure that there is an empty line at the end       |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| fix-encoding-pragma                                       | Remove encoding header from Python files               |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| flynt                                                     | Run flynt string format converter for Python           |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| gci                                                       | Consistent import ordering for Go files                |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| generate-airflow-diagrams                                 | Generate airflow diagrams                              |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| generate-airflowctl-datamodels                            | Generate Datamodels for AirflowCTL                     | *       |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| generate-airflowctl-help-images                           | Generate SVG from Airflow CTL Commands                 | *       |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| generate-openapi-spec                                     | Generate the FastAPI API spec                          | *       |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| generate-openapi-spec-fab                                 | Generate the FastAPI API spec for FAB                  | *       |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| generate-pypi-readme                                      | Generate PyPI README                                   |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| generate-tasksdk-datamodels                               | Generate Datamodels for TaskSDK client                 | *       |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| generate-volumes-for-sources                              | Generate volumes for docker compose                    |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| go-mockery                                                | Generate mocks for go                                  |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| go-mod-tidy                                               | Run go mod tidy                                        |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| gofmt                                                     | Format go code                                         |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| identity                                                  | Print checked files                                    |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| insert-license                                            | * Add license for all SQL files                        |         |
|                                                           | * Add license for all RST files                        |         |
|                                                           | * Add license for CSS/JS/JSX/PUML/TS/TSX               |         |
|                                                           | * Add license for all Shell files                      |         |
|                                                           | * Add license for all toml files                       |         |
|                                                           | * Add license for all Python files                     |         |
|                                                           | * Add license for all XML files                        |         |
|                                                           | * Add license for all Helm template files              |         |
|                                                           | * Add license for all YAML files except Helm templates |         |
|                                                           | * Add license for all Markdown files                   |         |
|                                                           | * Add license for all other files                      |         |
|                                                           | * Add license for all Go files                         |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| kubeconform                                               | Kubeconform check on our helm chart                    |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| lint-chart-schema                                         | Lint chart/values.schema.json file                     |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| lint-dockerfile                                           | Lint Dockerfile                                        |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| lint-helm-chart                                           | Lint Helm Chart                                        |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| lint-json-schema                                          | * Lint JSON Schema files                               |         |
|                                                           | * Lint NodePort Service                                |         |
|                                                           | * Lint Docker compose files                            |         |
|                                                           | * Lint chart/values.schema.json                        |         |
|                                                           | * Lint chart/values.yaml                               |         |
|                                                           | * Lint config_templates/config.yml                     |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| lint-markdown                                             | Run markdownlint                                       |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| mixed-line-ending                                         | Detect if mixed line ending is used (\r vs. \r\n)      |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| mypy-airflow-core                                         | * Run mypy for airflow-core                            | *       |
|                                                           | * Run mypy for airflow-core (manual)                   |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| mypy-airflow-ctl                                          | * Run mypy for airflow-ctl                             | *       |
|                                                           | * Run mypy for airflow-ctl (manual)                    |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| mypy-dev                                                  | * Run mypy for dev                                     | *       |
|                                                           | * Run mypy for dev (manual)                            |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| mypy-devel-common                                         | * Run mypy for devel-common                            | *       |
|                                                           | * Run mypy for devel-common (manual)                   |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| mypy-providers                                            | * Run mypy for providers                               | *       |
|                                                           | * Run mypy for providers (manual)                      |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| mypy-task-sdk                                             | * Run mypy for task-sdk                                | *       |
|                                                           | * Run mypy for task-sdk (manual)                       |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| pretty-format-json                                        | Format JSON files                                      |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| prevent-deprecated-sqlalchemy-usage                       | Prevent deprecated sqlalchemy usage                    |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| provider-version-compat                                   | Check for correct version_compat imports in providers  | *       |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| pylint                                                    | pylint                                                 |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| python-no-log-warn                                        | Check if there are no deprecate log warn               |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| replace-bad-characters                                    | Replace bad characters                                 |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| rst-backticks                                             | Check if RST files use double backticks for code       |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| ruff                                                      | Run 'ruff' for extremely fast Python linting           |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| ruff-format                                               | Run 'ruff format'                                      |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| shellcheck                                                | Check Shell scripts syntax correctness                 |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| trailing-whitespace                                       | Remove trailing whitespace at end of line              |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| ts-compile-lint-simple-auth-manager-ui                    | Compile / format / lint simple auth manager UI         |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| ts-compile-lint-ui                                        | Compile / format / lint UI                             |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| update-black-version                                      | Update black versions everywhere (manual)              |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| update-breeze-cmd-output                                  | Update breeze docs                                     |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| update-breeze-readme-config-hash                          | Update Breeze README.md with config files hash         |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| update-chart-dependencies                                 | Update chart dependencies to latest (manual)           |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| update-er-diagram                                         | Update ER diagram                                      | *       |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| update-in-the-wild-to-be-sorted                           | Sort INTHEWILD.md alphabetically                       |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| update-inlined-dockerfile-scripts                         | Inline Dockerfile and Dockerfile.ci scripts            |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| update-installed-providers-to-be-sorted                   | Sort and uniquify installed_providers.txt              |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| update-installers-and-pre-commit                          | Update installers and pre-commit to latest (manual)    |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| update-local-yml-file                                     | Update mounts in the local yml file                    |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| update-migration-references                               | Update migration ref doc                               | *       |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| update-providers-build-files                              | Update providers build files                           |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| update-providers-dependencies                             | Update dependencies for providers                      |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| update-pyproject-toml                                     | Update Airflow's meta-package pyproject.toml           |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| update-reproducible-source-date-epoch                     | Update Source Date Epoch for reproducible builds       |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| update-spelling-wordlist-to-be-sorted                     | Sort spelling_wordlist.txt                             |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| update-supported-versions                                 | Updates supported versions in documentation            |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| update-vendored-in-k8s-json-schema                        | Vendor k8s definitions into values.schema.json         |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| update-version                                            | Update versions in docs                                |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| validate-chart-annotations                                | Validate chart annotations                             |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| validate-operators-init                                   | No templated field logic checks in operator __init__   |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| yamllint                                                  | Check YAML files with yamllint                         |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+
| zizmor                                                    | Run zizmor to check for github workflow syntax errors  |         |
+-----------------------------------------------------------+--------------------------------------------------------+---------+

  .. END AUTO-GENERATED STATIC CHECK LIST

Using pre-commit
----------------

After installation, pre-commit hooks are run automatically when you commit the
code. But you can run pre-commit hooks manually as needed.

-   Run all checks on your staged files by using:

.. code-block:: bash

    pre-commit run

-   Run only mypy check on your staged files (in ``airflow/`` excluding providers) by using:

.. code-block:: bash

    pre-commit run mypy-airflow

-   Run only mypy checks on all files by using:

.. code-block:: bash

    pre-commit run mypy-airflow --all-files


-   Run all checks on all files by using:

.. code-block:: bash

    pre-commit run --all-files


-   Run all checks only on files modified in the last locally available commit in your checked out branch:

.. code-block:: bash

    pre-commit run --source=HEAD^ --origin=HEAD


-   Show files modified automatically by pre-commit when pre-commits automatically fix errors

.. code-block:: bash

    pre-commit run --show-diff-on-failure

-   Skip one or more of the checks by specifying a comma-separated list of
    checks to skip in the SKIP variable:

.. code-block:: bash

    SKIP=mypy-airflow-core,ruff pre-commit run --all-files


You can always skip running the tests by providing ``--no-verify`` flag to the
``git commit`` command.

To check other usage types of the pre-commit framework, see `Pre-commit website <https://pre-commit.com/>`__.

Disabling particular checks
---------------------------

In case you have a problem with running particular ``pre-commit`` check you can still continue using the
benefits of having ``pre-commit`` installed, with some of the checks disabled. In order to disable
checks you might need to set ``SKIP`` environment variable to coma-separated list of checks to skip. For example,
when you want to skip some checks (ruff/mypy for example), you should be able to do it by setting
``export SKIP=ruff,mypy-airflow-core,``. You can also add this to your ``.bashrc`` or ``.zshrc`` if you
do not want to set it manually every time you enter the terminal.

In case you do not have breeze image configured locally, you can also disable all checks that require breeze
the image by setting ``SKIP_BREEZE_PRE_COMMITS`` to "true". This will mark the tests as "green" automatically
when run locally (note that those checks will anyway run in CI).

Disabling goproxy for firewall issues
-------------------------------------

Sometimes your environment might not allow to connect to the ``goproxy`` server, which is used to
proxy/cache Go modules. When your firewall blocks go proxy it usually ends with message similar to:

.. code-block:: text

  lookup proxy.golang.org: i/o timeout

In such case, you can disable the ``goproxy`` by setting the
``GOPROXY`` environment variable to "direct". You can do it by running:

.. code-block:: bash

    export GOPROXY=direct

Alternatively if your company has its own Go proxy, you can set the ``GOPROXY`` to
your company Go proxy URL. For example:

.. code-block:: bash

    export GOPROXY=https://mycompanygoproxy.com

See `Go Proxy lesson <https://www.practical-go-lessons.com/chap-18-go-module-proxies#configuration-of-the-go-module-proxy>`__)
for more details on how to configure Go proxy - including setting multiple proxies.

You can add the variable to your ``.bashrc`` or ``.zshrc`` if you do not want to set it manually every time you
enter the terminal.

Manual pre-commits
------------------

Most of the checks we run are configured to run automatically when you commit the code. However,
there are some checks that are not run automatically and you need to run them manually. Those
checks are marked with ``manual`` in the ``Description`` column in the table below. You can run
them manually by running ``pre-commit run --hook-stage manual <hook-id>``.

Special pin-versions pre-commit
-------------------------------

There is a separate pre-commit ``pin-versions`` pre-commit which is used to pin versions of
GitHub Actions in the CI workflows.

This action requires ``GITHUB_TOKEN`` to be set, otherwise you might hit the rate limits with GitHub API, it
is also configured in a separate ``.pre-commit-config.yaml`` file in the
``.github`` directory as it requires Python 3.11 to run. It is not run automatically
when you commit the code but in runs as a separate job in the CI. However, you can run it
manually by running:

.. code-block:: bash

    export GITHUB_TOKEN=YOUR_GITHUB_TOKEN
    pre-commit run -c .github/.pre-commit-config.yaml --all-files --hook-stage manual --verbose


Mypy checks
-----------

When we run mypy checks locally when committing a change, one of the ``mypy-*`` checks is run, ``mypy-airflow``,
``mypy-dev``, ``mypy-providers``, ``mypy-airflow-ctl``, depending on the files you are changing. The mypy checks
are run by passing those changed files to mypy. This is way faster than running checks for all files (even
if mypy cache is used - especially when you change a file in Airflow core that is imported and used by many
files). However, in some cases, it produces different results than when running checks for the whole set
of files, because ``mypy`` does not even know that some types are defined in other files and it might not
be able to follow imports properly if they are dynamic. Therefore in CI we run ``mypy`` check for whole
directories (``airflow`` - excluding providers, ``providers``, ``dev`` and ``docs``) to make sure
that we catch all ``mypy`` errors - so you can experience different results when running mypy locally and
in CI. If you want to run mypy checks for all files locally, you can do it by running the following
command (example for ``airflow`` files):

.. code-block:: bash

  pre-commit run --hook-stage manual mypy-<FOLDER> --all-files

For example:

.. code-block:: bash

  pre-commit run --hook-stage manual mypy-airflow --all-files

To show unused mypy ignores for any providers/airflow etc, eg: run below command:

.. code-block:: bash
  export SHOW_UNUSED_MYPY_WARNINGS=true
  pre-commit run --hook-stage manual mypy-airflow --all-files

MyPy uses a separate docker-volume (called ``mypy-cache-volume``) that keeps the cache of last MyPy
execution in order to speed MyPy checks up (sometimes by order of magnitude). While in most cases MyPy
will handle refreshing the cache when and if needed, there are some cases when it won't (cache invalidation
is the hard problem in computer science). This might happen for example when we upgrade MyPY. In such
cases you might need to manually remove the cache volume by running ``breeze down --cleanup-mypy-cache``.

Running static code checks via Breeze
-------------------------------------

The static code checks can be launched using the Breeze environment.

You run the static code checks via ``breeze static-check`` or commands.

You can see the list of available static checks either via ``--help`` flag or by using the autocomplete
option.

Run the ``mypy`` check for the currently staged changes (in ``airflow/`` excluding providers):

.. code-block:: bash

     breeze static-checks --type mypy-airflow

Run the ``mypy`` check for all files:

.. code-block:: bash

     breeze static-checks --type mypy-airflow --all-files

Run the ``ruff`` check for the ``tests/core.py`` file with verbose output:

.. code-block:: bash

     breeze static-checks --type ruff --file tests/core.py --verbose

Run the ``ruff`` check for the ``tests.core`` package with verbose output:

.. code-block:: bash

     breeze static-checks --type ruff --file tests/core/* --verbose

Run the ``ruff-format`` check for the files ``airflow/example_dags/example_bash_operator.py`` and
``airflow/example_dags/example_python_operator.py``:

.. code-block:: bash

     breeze static-checks --type ruff-format --file airflow/example_dags/example_bash_operator.py \
         airflow/example_dags/example_python_operator.py

Run all checks for the currently staged files:

.. code-block:: bash

     breeze static-checks

Run all checks for all files:

.. code-block:: bash

    breeze static-checks --all-files

Run all checks for last commit:

.. code-block:: bash

     breeze static-checks --last-commit

Run all checks for all changes in my branch since branched from main:

.. code-block:: bash

     breeze static-checks --type mypy-airflow --only-my-changes

More examples can be found in
`Breeze documentation <../dev/breeze/doc/03_developer_tasks.rst#running-static-checks>`_


Debugging pre-commit check scripts requiring image
--------------------------------------------------

Those commits that use Breeze docker image might sometimes fail, depending on your operating system and
docker setup, so sometimes it might be required to run debugging with the commands. This is done via
two environment variables ``VERBOSE`` and ``DRY_RUN``. Setting them to "true" will respectively show the
commands to run before running them or skip running the commands.

Note that you need to run pre-commit with --verbose command to get the output regardless of the status
of the static check (normally it will only show output on failure).

Printing the commands while executing:

.. code-block:: bash

     VERBOSE="true" pre-commit run --verbose ruff

Just performing dry run:

.. code-block:: bash

     DRY_RUN="true" pre-commit run --verbose ruff

-----------

Once your code passes all the static code checks, you should take a look at `Testing documentation <09_testing.rst>`__
to learn about various ways to test the code.
