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
# retry MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import asyncio
from functools import wraps
from config.constants import MAX_RETRIES, RETRY_DELAYS
from utils.logger import get_logger

logger = get_logger()


def retry_async(func):

    @wraps(func)
    async def wrapper(*args, **kwargs):

        for attempt in range(MAX_RETRIES):
            try:
                return await func(*args, **kwargs)
            
            except Exception as e:

                if attempt == MAX_RETRIES - 1:
                    logger.error(f"Max retries reached: {e}")
                    raise

                delay = RETRY_DELAYS[attempt]
                logger.warning(f"Retrying in {delay}s due to {e}")

                await asyncio.sleep(delay)
    
    return wrapper
