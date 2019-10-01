# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 16:30:44 2019

@author: nanan
"""
import sqlite3 as sq
import csv

def connect_database():    
    #database
    try:
        connection = sq.connect('../data/warm-up-DB-205.db')
        print("Database was created successfully locally")
        
        
    except sq.Error as err:
        print("Check the database conncetion, error", err)
    
    c = connection.cursor()
    
    #Drop the tables
    c.execute("""DROP TABLE IF EXISTS tblCrimes;""")
    connection.commit()
    c.execute("""DROP TABLE IF EXISTS tblOffenseCode;""")
    connection.commit()
    
    #Creating the first table
    c.execute("""CREATE TABLE IF NOT EXISTS tblCrimes
                  (fld_incident_id TEXT,
                  fld_offense_id TEXT,
                  fld_first_occurence_date TEXT,
                  fld_reported_date TEXT,
                  fld_incident_address TEXT,
                  fld_precinct_id INTEGER,
                  fld_neighborhood_id TEXT,
                  fld_offense_code TEXT)""")
    
    print("Done Creating tblCrimes")
    
    #Creating the second table
    c.execute("""CREATE TABLE tblOffenseCode
                  (fld_offense_type TEXT,
                  fld_offense_category TEXT,
                  fld_is_crime INTEGER,
                  fld_is_traffic INTEGER,
                  fld_offense_code INTEGER)""")
    print("Done Creating tblOffenseCode")
    
    #Open csv for crimes
    with open("../data/crime_final.csv", newline = '') as csvfile:
        crime_info = csv.reader(csvfile)
        next(crime_info)
        for crime_row in crime_info:
            time = crime_row[3]
            date = time.split('/')
            #FIRST OCCURENCE DATE
            if (len(date[0]) == 1):
                month = '0' + date[0]
            else:
                month = date[0]
            if (len(date[1]) == 1):
                day = '0' + date[1]
            else:
                day = date[1]
            final_date = '20' + date[2].split(' ')[0] + '-' + month + '-' + day
            first_raw_time = date[2].split(' ')[1].split(":")
            if len(first_raw_time[0]) == 1:
                first_hour = '0'+ first_raw_time[0]
            else:
                first_hour = first_raw_time[0]
            final_time = first_hour + ':' + first_raw_time[1] + ':00' + '.000'
            final_date_insert = final_date + ' ' + final_time
            
            #REPORTED DATE
            reported_date = crime_row[4]
            r_date = reported_date.split('/')
            if (len(r_date[0]) == 1):
                month = '0' + r_date[0]
            else:
                month = r_date[0]
            if (len(r_date[1]) == 1):
                day = '0' + r_date[1]
            else:
                day = r_date[1]
            report_date = '20' + r_date[2].split(' ')[0] + '-' + month + '-' + day
            raw_time = r_date[2].split(' ')[1].split(':')
            if len(raw_time[0]) == 1:
                hour = '0'+ raw_time[0]
            else:
                hour = raw_time[0]
            report_time = hour + ':' + raw_time[1] + ':00' + '.000'
            final_report_insert = report_date + ' ' + report_time
            to_insert_crime = (crime_row[1], crime_row[2], final_date_insert, final_report_insert, crime_row[5], int(crime_row[6]), crime_row[7], crime_row[8])
            #the insert query
            c.execute("""INSERT INTO tblCrimes (fld_incident_id, fld_offense_id, fld_first_occurence_date, fld_reported_date, fld_incident_address, fld_precinct_id, fld_neighborhood_id, fld_offense_code) 
               VALUES(?,?,?,?,?,?,?,?)""", to_insert_crime)
        
    connection.commit()
    print("Done Inserting into tblCrimes")
    
    #Open csv for crimes
    with open("../data/offense_codes_final.csv", newline = '') as csvfile:
        offense_info = csv.reader(csvfile)
        next(offense_info)
        for offense_row in offense_info:
            #the tuple to use for inserting the data into the table
            to_insert_offense = (offense_row[1], offense_row[2], int(offense_row[3]), int(offense_row[4]), int(offense_row[5]))
            #the insert query
            c.execute("""INSERT INTO tblOffenseCode (fld_offense_type, fld_offense_category, fld_is_crime, fld_is_traffic, fld_offense_code) 
               VALUES(?,?,?,?,?)""", to_insert_offense)
        
    connection.commit()
    print("Done Inserting into tblOffenseCode")
    connection.close()