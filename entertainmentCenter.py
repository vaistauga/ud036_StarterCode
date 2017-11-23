import media
import fresh_tomatoes

#Video
inception = media.Video(        "Inception",
                                "Go into the dreams of a bussinessman to change his mind about something",
                                "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                                "https://www.youtube.com/watch?v=66TuSJo4dZM")

interstellar = media.Video(     "Intersellar",
                                "Travel through the black hole to save humanity",
                                "https://images-na.ssl-images-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SY1000_SX675_AL_.jpg",
                                "https://www.youtube.com/watch?v=0vxOhd4qlnA")

burnAfterReading = media.Video( "Burn After Reading",
                                "Not so smart people causing havock by blackmail",
                                "https://images-na.ssl-images-amazon.com/images/M/MV5BMTczNjQxODE0N15BMl5BanBnXkFtZTcwMzIxMjc3MQ@@._V1_SY1000_CR0,0,665,1000_AL_.jpg",
                                "https://www.youtube.com/watch?v=SVCHSiRWjJM")

fargo = media.Video(            "Fargo",
                                "A murder in  a small town caused unprecedented brutality in a fun way",
                                "https://images-na.ssl-images-amazon.com/images/M/MV5BMTRmNGFlZGUtODY5ZC00YjJlLTk0ZDMtYjBhZDI1OGQ5YjU1XkEyXkFqcGdeQXVyMjk3NTUyOTc@._V1_.jpg",
                                "https://www.youtube.com/watch?v=u4Je2WxsqWA")

batmanVSSuperman = media.Video( "Batman V.S. Superman",
                                "Rich human fights good looking alien who is imortal to everything but dies in the end",
                                "https://images-na.ssl-images-amazon.com/images/M/MV5BYThjYzcyYzItNTVjNy00NDk0LTgwMWQtYjMwNmNlNWJhMzMyXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                                "https://www.youtube.com/watch?v=X7SiuQxhAjg")

SuckerPunch = media.Video (     "Suckerpunch",
                                "Explores disociation as a stress coping mechanism with allot of visual effects",
                                "https://images-na.ssl-images-amazon.com/images/M/MV5BNDEwNGRlNjQtZjI4OC00ZmMxLWEyYmQtNGI1NDk4YmUyYTNkXkEyXkFqcGdeQXVyNjQ2MjQ5NzM@._V1_SY1000_CR0,0,676,1000_AL_.jpg",
                                "https://www.youtube.com/watch?v=9k10AzCcMOM")
#Music
ParovStelar = media.Music(      "Company of Heroes 2",
                                "Real time strategy game which strikes an excelent balance betweem tactics and strategy",
                                "https://images-na.ssl-images-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SY1000_SX675_AL_.jpg",
                                "null")

#Games
companyOfHeroes2 = media.Game(  "Company of Heroes 2",
                                "Real time strategy game which strikes an excelent balance betweem tactics and strategy",
                                "https://images-na.ssl-images-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SY1000_SX675_AL_.jpg",
                                "null")

movies = [inception, interstellar, burnAfterReading, fargo, batmanVSSuperman, SuckerPunch, ParovStelar, companyOfHeroes2]
fresh_tomatoes.open_movies_page(movies)
