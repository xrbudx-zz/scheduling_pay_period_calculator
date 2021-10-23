from datetime import date, timedelta
import pandas as pd
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

scheduling_start_date = pd.to_datetime(config['scheduling_period']['start_date'])
scheduling_period_frequency = int(config['scheduling_period']['frequency'])

pay_period_start_date = pd.to_datetime(config['pay_period']['start_date'])
pay_period_frequency = int(config['pay_period']['frequency'])

min_punch_apply_date = pd.to_datetime(config['min_punch_apply_date']['min_pad']) # get min(punch_apply_date) from historic timesheet

def calc(start_date, frequency):
    frequency = pd.Timedelta(frequency, unit = "w").days

    while start_date > min_punch_apply_date:
        start_date = start_date - timedelta(frequency)
        print (start_date.date())

print("\nMinimum Punch Apply Date in Historic Timesheet: " + str(min_punch_apply_date.date()))

print ("\nScheduling Period Starting Date: " + str(scheduling_start_date.date()) + "\nScheduling Period Frequency: " + str(scheduling_period_frequency))
calc(scheduling_start_date, scheduling_period_frequency)

print("____________________________________________________________________________________________________________________")
print ("\nPay Period Starting Date: " + str(pay_period_start_date.date()) + "\nPay Period Frequency: " + str(pay_period_frequency))
calc(pay_period_start_date, pay_period_frequency)