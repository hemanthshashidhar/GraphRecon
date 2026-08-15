from graphrecon.runtime.runtime import Runtime


runtime = Runtime()

runtime.scan("https://quotes.toscrape.com")

responses = runtime.response_collector.cache.all()

print(f"Cached responses: {len(responses)}")

for response in responses: 

    if response.request.resource_type != "script":
        continue

    print("=" * 80)
    print(response.url)

    try:
        text = response.text()

        print(text[:300])

    except Exception as exc:
        print(exc)
