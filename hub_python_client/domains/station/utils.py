from .entity import Registry


def build_registry_client_connection_string_from_registry(entity: Registry):
    url = f'https://{entity.host}/api/v2.0/'
    return f'{entity.account_name}:{entity.account_secret}@{url}'
