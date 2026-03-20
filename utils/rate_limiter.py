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
# rate_limiter MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import time
from collections import defaultdict
from config.constants import DEFAULT_RATE_LIMIT, RATE_LIMIT_WINDOW


class RateLimiter:

    def __init__(self):
        self.requests = defaultdict(list)
    
    def is_allowed(self, key: str):

        now = time.time()
        window_start = now - RATE_LIMIT_WINDOW

        timestamps = self.requests[key]

        # remove expired timestamps
        self.requests[key] = [
            ts for ts in timestamps if ts > window_start
        ]

        if len(self.requests[key]) >= DEFAULT_RATE_LIMIT:
            return False
        
        self.requests[key].append(now)

        return True
