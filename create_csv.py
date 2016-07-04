#!/usr/bin/env python

import billboard
import time

def retrieve_songs():
    songs = [];
    chart = billboard.ChartData('hot-100')
    count = 0
    while chart.previousDate and count < 10:
        print("week: "+chart.previousDate)
        add_date_to_songs(chart.entries,chart.previousDate)
        songs.extend(chart.entries)
        chart = billboard.ChartData('hot-100', chart.previousDate)
        time.sleep(2)  # Throttle requests
        count += 1

    return songs


def remove_duplicates(songs):
    return list(set(songs))

def add_date_to_songs(songs, date):
    for song in songs:
        song.date = date

def save_json(songs):
    f = open('songs.json', 'w')
    for song in songs:
        f.writelines(song.to_JSON())

if __name__ == "__main__":
    songs = retrieve_songs()
    songs = remove_duplicates(songs)
    save_json(songs)

