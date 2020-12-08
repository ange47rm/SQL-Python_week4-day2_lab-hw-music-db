
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist_repository.delete_all ()

artist_1 = Artist ('Nas')
artist_repository.create (artist_1)

artist_2 = Artist ('Jay-Z')
artist_repository.create (artist_2)

artist_3 = Artist ('2Pac')
artist_repository.create (artist_3) # TESTs PASSED (3 items created)

# artist_repository.delete_id (3) - TEST PASSED (1 item deleted)


# artist_repository.delete_all() - TEST PASSED (all items deleted)


# all_artists = artist_repository.select_all()
# for artist in all_artists:
#     print (artist.__dict__) - TEST PASSED (all artists in db are put in list)


# artist = artist_repository.select(2)
# print (artist.__dict__) -- TEST PASSED (prints {'name': 'Jay-Z', 'id': 2})


album_1 = Album ('Illmatic', 'Hip-Hop', artist_1)
album_repository.create (album_1)

album_2 = Album ('4:44', 'Hip-Hop', artist_2)
album_repository.create (album_2)

album_3 = Album ('All Eyez On Me', 'Hip-Hop', artist_3)
album_repository.create (album_3) # TEST PASSED (3 albums created)


# all_albums = album_repository.select_all()
# for album in all_albums:
#     print (album.__dict__) -- TEST PASSED (displays 3 albums, however artist)

# album_repository.delete_all () -- TEST PASSED (all 3 albums are deleted)

# album = album_repository.select (1)
# print (album.__dict__) -- TEST PASSED (finds album with ID 1, Illmatic)

all_albums = album_repository.select_all()
for album in all_albums:
    print (album.__dict__)








