import bitlyshortener

tokens_pool = ['76a0cda5c7cb80b51618905b312c8bd68b41d5b9']  # Use your ow

shortener = bitlyshortener.Shortener(tokens=tokens_pool, max_cache_size=256)

async def bitly(url):
    return shortener._shorten_url(url)