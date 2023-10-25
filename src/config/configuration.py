from environs import Env


class Config:
    def __init__(self):
        env = Env()
        env.read_env()
        self.__token: str = env("BOT_TOKEN")
        self.__developer_id: int = env.int("DEVELOPER_ID")
        self.__db_name: str = env("DB_NAME")
        self.__db_password: str = env("DB_PASSWORD")
        self.__username: str = env("DB_USERNAME")
        self.__ngrok_tunnel_url: str = env("NGROK_TUNNEL_URL")
        self.__webhook_path: str = f"/bot/{self.__token}"
        self.__webhook_url: str = f"{self.__ngrok_tunnel_url}{self.__webhook_path}"

    def get_token(self) -> str:
        return self.__token

    def get_webhook_path(self):
        return self.__webhook_path

    def get_ngrok_tunnel_url(self) -> str:
        return self.__ngrok_tunnel_url

    def get_webhook_url(self) -> str:
        return self.__webhook_url

    def get_username(self) -> str:
        return self.__username

    def get_db_name(self) -> str:
        return self.__db_name

    def get_db_password(self) -> str:
        return self.__db_password

    def get_developer_id(self) -> int:
        return self.__developer_id


def get_config():
    return Config()
