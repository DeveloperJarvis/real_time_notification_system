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
# notification_log MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.sql import func
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()
from database.db import Base


class NotificationLog(Base):
    __tablename__ = "notification_logs"

    notification_id = Column(String, primary_key=True, index=True)
    user_id = Column(String, index=True)

    channel = Column(String)
    status = Column(String)

    retry_count = Column(Integer, default=0)

    created_at = Column(DateTime(timezone=True),
                        server_default=func.now())
    
    def __repr__(self):
        return f"<NotificationLog id={self.notification_id} status={self.status}>"
