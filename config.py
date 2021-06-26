from environs import Env

env = Env()
env.read_env()

spotify_client_id = env.str("spotify_client_id")
spotify_client_secret = env.str("spotify_client_secret")