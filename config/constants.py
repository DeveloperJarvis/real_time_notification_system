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
# constants MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------


# Notification Channels
PUSH_CHANNEL = "push"
EMAIL_CHANNEL = "email"
SMS_CHANNEL = "sms"

# Retry Configuration
MAX_RETRIES = 3
RETRY_DELAYS = [5, 30, 300]

# Rate Limiting
DEFAULT_RATE_LIMIT = 100
RATE_LIMIT_WINDOW = 60

# Websocket
MAX_CONNECTIONS = 10000
