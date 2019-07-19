from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
  # return HttpResponse('Wordcount Views Hello')
  return render(request, 'wordcount/home.html')

def count(request):
  # return HttpResponse('Wordcount Views count')
  
  fulltext = request.GET['fulltext']
  print(fulltext)

  wordlist = fulltext.split()

  wordlistdic = {}
  for word in wordlist:
    if word in wordlistdic:
      wordlistdic[word] += wordlistdic[word] 
    else:
      wordlistdic[word] = 1

  s_wordlistdic = sorted(wordlistdic.items(), key=lambda x:x[1], reverse=True)
  return render(request, 'wordcount/count.html', {'fulltext':fulltext, 'wordcount': len(wordlist), 'wordlistdic': s_wordlistdic})
