## **RDB or Redis Database Backup**
It is like a snapshot of database at a specific time interval like in every hour or 2 hours.
At set times, Redis takes a quick snapshot of your current RAM data and store it as  single compact file.
If redis crashes or reboots, we can restore the data from this snapshot.


## **AOF or Append Only File**
Think of AOF like a running logbook or diary that records every single change as it happens.
Every time you add , udpate or delete data, redis write exact command to continuous text file.
Almost zero data loss because every write command is saved instantly or witing 1 second.


## **Quick comparison between RDB and AOF**
1. RDB is like photo album and AOF is a daily diary.
2. Data safety in RDB is medium, while AOF is high.
3. RDB file size is small and compact, but AOF is large and slow.
4. RDB is blazzing fast, but AOF is slower.