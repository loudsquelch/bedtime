import soco
import logging
import time

logging.basicConfig()
logging.getLogger("soco").setLevel(logging.INFO)

# import soco.config

# soco.config.CACHE_ENABLED = False

TARGET_VOLUME = 5
TARGET_SONG_TITLE = "Forest Mist Brown Noise Loop (No Fade)"

# Turn off UFW
speakers = soco.discover()
if speakers is None:
    print("Is your firewall blocking me?")

speaker = [speaker for speaker in speakers if speaker.player_name == "Bedroom"][
    0
]
is_playing = (
    speaker.get_current_transport_info()["current_transport_state"] == "PLAYING"
)

faves = speaker.music_library.get_sonos_favorites()
song = [fav for fav in faves if fav.title == TARGET_SONG_TITLE][0]

if not is_playing:
    # Set to volume of zero
    time.sleep(speaker.ramp_to_volume(0) + 3)
    # Clear queue
    speaker.clear_queue()
    # Get queue
    queue = speaker.get_queue()
    print(queue)
    # Add to queue
    speaker.add_to_queue(song)
    speaker.play_from_queue(0)
    # Ramp up volume
    speaker.ramp_to_volume(TARGET_VOLUME)
    # Set to REPEAT_ALL
    if speaker.play_mode != "REPEAT_ALL":
        speaker.play_mode = "REPEAT_ALL"
