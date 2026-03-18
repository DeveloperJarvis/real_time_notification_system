@echo off

REM Root directory
@REM set ROOT=log_pattern_detection_tool
set ROOT=.

REM Create directories if they do not exist
call :create_folder "%ROOT%"
call :create_folder "%ROOT%\docs"
call :create_folder "%ROOT%\logs"
call :create_folder "%ROOT%\tests"
call :create_folder "%ROOT%\config"
call :create_folder "%ROOT%\notification_api"
call :create_folder "%ROOT%\notification_api\routes"
call :create_folder "%ROOT%\notification_api\schemas"
call :create_folder "%ROOT%\notification_api\services"
call :create_folder "%ROOT%\notification_api\middleware"
call :create_folder "%ROOT%\producers"
call :create_folder "%ROOT%\broker"
call :create_folder "%ROOT%\workers"
call :create_folder "%ROOT%\delivery"
call :create_folder "%ROOT%\models"
call :create_folder "%ROOT%\websocket_gateway"
call :create_folder "%ROOT%\database"
call :create_folder "%ROOT%\database\migrations"
call :create_folder "%ROOT%\database\repositories"
call :create_folder "%ROOT%\utils"

REM Create files only if they do not exist
REM Python source files (with header)
call :create_py_file "%ROOT%\main.py"

call :create_py_file "%ROOT%\config\__init__.py"
call :create_py_file "%ROOT%\config\constants.py"
call :create_py_file "%ROOT%\config\settings.py"

call :create_py_file "%ROOT%\notification_api\__init__.py"
call :create_py_file "%ROOT%\notification_api\app.py"
call :create_py_file "%ROOT%\notification_api\routes\__init__.py"
call :create_py_file "%ROOT%\notification_api\routes\notification_routes.py"
call :create_py_file "%ROOT%\notification_api\schemas\__init__.py"
call :create_py_file "%ROOT%\notification_api\schemas\notification_schema.py"
call :create_py_file "%ROOT%\notification_api\services\__init__.py"
call :create_py_file "%ROOT%\notification_api\services\publish_service.py"
call :create_py_file "%ROOT%\notification_api\middleware\__init__.py"
call :create_py_file "%ROOT%\notification_api\middleware\auth_middleware.py"

call :create_py_file "%ROOT%\producers\__init__.py"
call :create_py_file "%ROOT%\producers\chat_service_producer.py"
call :create_py_file "%ROOT%\producers\order_service_producer.py"
call :create_py_file "%ROOT%\producers\payment_service_producer.py"

call :create_py_file "%ROOT%\broker\__init__.py"
call :create_py_file "%ROOT%\broker\kafta_client.py"
call :create_py_file "%ROOT%\broker\topics.py"
call :create_py_file "%ROOT%\broker\publisher.py"

call :create_py_file "%ROOT%\workers\__init__.py"
call :create_py_file "%ROOT%\workers\notification_worker.py"
call :create_py_file "%ROOT%\workers\email_worker.py"
call :create_py_file "%ROOT%\workers\sms_worker.py"

call :create_py_file "%ROOT%\delivery\__init__.py"
call :create_py_file "%ROOT%\delivery\push_delivery_service.py"
call :create_py_file "%ROOT%\delivery\email_delivery_service.py"
call :create_py_file "%ROOT%\delivery\sms_delivery_service.py"

call :create_py_file "%ROOT%\models\__init__.py"
call :create_py_file "%ROOT%\models\user_device.py"
call :create_py_file "%ROOT%\models\notification_log.py"

call :create_py_file "%ROOT%\websocket_gateway\__init__.py"
call :create_py_file "%ROOT%\websocket_gateway\gateway_server.py"
call :create_py_file "%ROOT%\websocket_gateway\connection_manager.py"

call :create_py_file "%ROOT%\database\__init__.py"
call :create_py_file "%ROOT%\database\db.py"
call :create_py_file "%ROOT%\database\migrations\__init__.py"
call :create_py_file "%ROOT%\database\repositories\__init__.py"
call :create_py_file "%ROOT%\database\repositories\device_repository.py"
call :create_py_file "%ROOT%\database\repositories\notification_repository.py"

call :create_py_file "%ROOT%\utils\__init__.py"
call :create_py_file "%ROOT%\utils\logger.py"
call :create_py_file "%ROOT%\utils\retry.py"
call :create_py_file "%ROOT%\utils\rate_limiter.py"

call :create_py_file "%ROOT%\tests\__init__.py"
call :create_py_file "%ROOT%\tests\test_api.py"
call :create_py_file "%ROOT%\tests\test_workers.py"
call :create_py_file "%ROOT%\tests\test_delivery.py"

REM Setup file (with header) generalized body
call :create_setup_py_file "%ROOT%\setup.py"

REM Non-Python files (empty)
call :create_file "%ROOT%\logs\logs.log"

call :create_file "%ROOT%\docs\sequence-diagrams.md"
call :create_file "%ROOT%\docs\system_design.md"

call :create_file "%ROOT%\requirements.txt"
call :create_file "%ROOT%\README.md"
call :create_file "%ROOT%\LICENSE"
call :create_file "%ROOT%\docker-compose.yml"
call :create_file "%ROOT%\.env"

echo Folder structure created (existing files and folders were preserved).
goto :eof

REM -------------------------------------------
REM Create folders if does not exist
REM -------------------------------------------

:create_folder
if not exist "%~1" (
    mkdir "%~1"
)

REM -------------------------------------------
REM Create empty file if it does not exist
REM -------------------------------------------

:create_file
if not exist "%~1" (
    type nul > "%~1"
)

exit /b

REM -------------------------------------------
REM Create python file with GPL header
REM -------------------------------------------
:create_py_file
if exist "%~1" exit /b

set FILEPATH=%~1
set FILENAME=%~n1

(
echo # --------------------------------------------------
echo # -*- Python -*- Compatibility Header
echo #
echo # Copyright ^(C^) 2023 Developer Jarvis ^(Pen Name^)
echo #
echo # This file is part of the Real-Time Notification System Library. This library is free
echo # software; you can redistribute it and/or modify it under the
echo # terms of the GNU General Public License as published by the
echo # Free Software Foundation; either version 3, or ^(at your option^)
echo # any later version.
echo #
echo # This program is distributed in the hope that it will be useful,
echo # but WITHOUT ANY WARRANTY; without even the implied warranty of
echo # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
echo # GNU General Public License for more details.
echo #
echo # You should have received a copy of the GNU General Public License
echo # along with this program. If not, see ^<https://www.gnu.org/licenses/^>.
echo #
echo # SPDX-License-Identifier: GPL-3.0-or-later
echo #
echo # Real-Time Notification System - Push notifications using pub/sub model
echo # Skills: messaging systems, async IO
echo #
echo # Author: Developer Jarvis ^(Pen Name^)
echo # Contact: https://github.com/DeveloperJarvis
echo #
echo # --------------------------------------------------
echo.
echo # --------------------------------------------------
echo # %FILENAME%% MODULE
echo # --------------------------------------------------
echo.
echo # --------------------------------------------------
echo # imports
echo # --------------------------------------------------
echo.
) > "%FILEPATH%"

exit /b

REM -------------------------------------------
REM Create setup python file with GPL header
REM -------------------------------------------
:create_setup_py_file
if exist "%~1" exit /b

set FILEPATH=%~1
set FILENAME=%~n1

(
echo # --------------------------------------------------
echo # -*- Python -*- Compatibility Header
echo #
echo # Copyright ^(C^) 2023 Developer Jarvis ^(Pen Name^)
echo #
echo # This file is part of the Real-Time Notification System Library. This library is free
echo # software; you can redistribute it and/or modify it under the
echo # terms of the GNU General Public License as published by the
echo # Free Software Foundation; either version 3, or ^(at your option^)
echo # any later version.
echo #
echo # This program is distributed in the hope that it will be useful,
echo # but WITHOUT ANY WARRANTY; without even the implied warranty of
echo # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
echo # GNU General Public License for more details.
echo #
echo # You should have received a copy of the GNU General Public License
echo # along with this program. If not, see ^<https://www.gnu.org/licenses/^>.
echo #
echo # SPDX-License-Identifier: GPL-3.0-or-later
echo #
echo # Real-Time Notification System - Push notifications using pub/sub model
echo # Skills: messaging systems, async IO
echo #
echo # Author: Developer Jarvis ^(Pen Name^)
echo # Contact: https://github.com/DeveloperJarvis
echo #
echo # --------------------------------------------------
echo.
echo # --------------------------------------------------
echo # %FILENAME%% MODULE
echo # --------------------------------------------------
echo.
echo # --------------------------------------------------
echo # imports
echo # --------------------------------------------------
echo from setuptools import setup, find_packages
echo .
echo .
echo setup^(
echo     name="",
echo     version="0.1.0",
echo     description="",
echo     author="Developer Jarvis",
echo     author_email="developerjarvis@github.com",
echo     license="GPL-3.0-or-later",
echo     packages=find_packages^(
echo         exclude=^("tests*", "logs*",^)
echo     ^),
echo     python_requires=">=3.9",
echo     install_requires=[],
echo     extras_require={
echo         "dev": [
echo             "pytest",
echo             "black",
echo             "flake8",
echo             "mypy",
echo         ]
echo     },
echo     classifiers=[
echo         "Programming Language :: Python :: 3",
echo         "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
echo         "Operating System :: OS Independent",
echo     ],
echo ^)
echo .
) > "%FILEPATH%"

exit /b
