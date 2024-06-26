import requests as r
from dataclasses import dataclass

@dataclass
class Quote:
    quote: str
    author:str
def get_quote(url:str)->Quote:
    request:r.Response=r.get(url=url)
    data:dict=request.json()
    content:str=data.setdefault('content','......')
    author:str=data.setdefault('author','......')
    return Quote(content,author)
if __name__ == '__main__':
    url: str = 'https://api.quotable.io/random'
    quote:Quote=get_quote(url)
    print('Quote:',quote.quote)
    print('Author:',quote.author)




