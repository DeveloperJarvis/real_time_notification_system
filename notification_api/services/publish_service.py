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
# publish_service MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import uuid

from broker.publisher import publish_event
from broker.topics import PUSH_TOPIC, EMAIL_TOPIC, SMS_TOPIC
from notification_api.schemas.notification_schema import NotificationRequest
from utils.logger import get_logger

logger = get_logger()


async def publish_notification(request: NotificationRequest):

    event = {
        "notification_id": str(uuid.uuid4()),
        "user_id": request.user_id,
        "event_type": request.event_type,
        "payload": request.payload
    }

    if request.channel == "push":
        topic = PUSH_TOPIC
    
    elif request.channel == "email":
        topic = EMAIL_TOPIC
    
    elif request.channel == "sms":
        topic = SMS_TOPIC
    
    else:
        raise ValueError("Invalid notification channel")

    await publish_event(topic, event)

    logger.info(f"Notification published to {topic}")
