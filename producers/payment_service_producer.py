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
# payment_service_producer MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import uuid
from broker.publisher import publish_event
from broker.topics import PUSH_TOPIC


async def publish_payment_notification(user_id: str,
                        payment_id: str, amount: float):
    
    event = {
        "notification_id": str(uuid.uuid4()),
        "event_type": "PAYMENT_SUCCESS",
        "user_id": user_id,
        "payload": {
            "payment_id": payment_id,
            "amount": amount
        }
    }

    await publish_event(PUSH_TOPIC, event)
