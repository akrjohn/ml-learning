import TGHelper

movieList = []
TGHelper.tgPageIterator('http://tamilgun.tips/categories/hd-movies/', movieList)
TGHelper.iterateMovies(movieList)