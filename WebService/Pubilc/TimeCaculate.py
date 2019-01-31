#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from datetime import datetime, timedelta

class TimeRange(object):

    def get_recent_days(self, days):
        # 从现在往前倒推n天的日期

        startDate = (datetime.now() - timedelta(days=days)).date()
        endDate = datetime.now().date()
        return startDate,endDate

if __name__ == "__main__":
    print(TimeRange().get_recent_days(7)[0])