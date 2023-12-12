from .entity import Registry


def buildRegistryClientConnectionStringFromRegistry(entity: Registry):
    url = f'https://{entity.host}/api/v2.0/'
    return f'{entity.account_name}:{entity.account_secret}@{url}'
