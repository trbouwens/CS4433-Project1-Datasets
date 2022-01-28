# Project 1 - Dataset Generator

#### This script ste generates 3 data sets (CSVs). They are structured as follows:

### MyPage

| Name        | Description                                                                                                               |
|-------------|---------------------------------------------------------------------------------------------------------------------------|
| ID          | unique  sequential  number  (integer)  from  1  to 200,000 indicating the owner of the page (there will be 200,000 lines) |
| Name        | characters of length between 10 and 20 (do not use commas inside this string)                                             |
| Nationality | characters of length between 10 and 20 (do not use commas inside this string)                                             |
| CountryCode | number (integer) between 1 and 50                                                                                         |
| Hobby       | sequence of characters of length between 10 and 20                                                                        |

### Friends

| Name             | Description                                                                                                                                                                                                |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FriendRel        | unique sequential number (integer) taken from value in the range from 1 to 20,000,000 (the file has 20,000,000 lines and thus friend relationships)                                                        |
| PersonID         | Person-ID of a person who has a Facebook page, i.e., from 1 to 200,000 people                                                                                                                              |
| MyFriend         | References ID of a person that you are friend with, i.e., from 1 to 200,000. This relation is not mutually necessarily, i.e., it just indicates that you declare that you are friends with this friend ID. |
| DateofFriendship | random number (integer; or some other sequential data type to use as date) between 1 and 1,000,000  to indicate when the friendship started                                                                |
| Desc             | text of characters of length between 20 and 50 explaining the type of friendship:  college-friend, girlfriend, family, etc                                                                                 |

### AccessLog

| Name         | Description                                                                                                                     |
|--------------|---------------------------------------------------------------------------------------------------------------------------------|
| AccessId     | unique sequential number (integer) from 1 to 10,000,000                                                                         |
| ByWho        | References the Id of the person who has accessed the Facebook page                                                              |
| WhatPage     | References the Id of the page that was accessed                                                                                 |
| TypeOfAccess | text  of  characters  of  length  between  20  and  50 explaining  if  just  viewed,  left  a  note,  added  a friendship, etc. |
| AccessTime   | random number between 1 and 1,000,000 (or epoch time)                                                                           |
