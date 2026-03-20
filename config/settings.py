# --------------------------------------------------
# -*- Python -*- Compatibility Header
#
# Copyright (C) 2023 Developer Jarvis (Pen Name)
#
# This file is part of the Real-Time Notification System Library. This library is free
# software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Real-Time Notification System - Push notifications using pub/sub model
# Skills: messaging systems, async IO
#
# Author: Developer Jarvis (Pen Name)
# Contact: https://github.com/DeveloperJarvis
#
# --------------------------------------------------

# --------------------------------------------------
# settings MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    APP_NAME = os.getenv("APP_NAME")
    ENVIRONMENT = os.getenv("ENVIRONMENT")
    DEBUG = os.getenv("DEBUG") == "True"

    API_HOST = os.getenv("API_HOST")
    API_PORT = os.getenv("API_PORT")

    # Kafka
    KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
    KAFKA_NOTIFICATION_TOPIC = os.getenv("KAFKA_NOTIFICATION_TOPIC")
    KAFKA_EMAIL_TOPIC = os.getenv("KAFKA_EMAIL_TOPIC")
    KAFKA_SMS_TOPIC = os.getenv("KAFKA_SMS_TOPIC")

    # Database
    DATABASE_URL = os.getenv("DATABASE_URL")

    # Redis
    REDIS_HOST = os.getenv("REDIS_HOST")
    REDIS_PORT = os.getenv("REDIS_PORT")

    # Security
    API_KEY = os.getenv("API_KEY")

    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL")
    LOG_FILE = os.getenv("LOG_FILE")


settings = Settings()
