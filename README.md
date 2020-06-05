# RSASecAnalyzer

Реализация системы анализа корректности выбранных параметров в криптосистеме RSA.
Выполнена на языке python в формате Jupyter Notebook.

Некоторые реализации вспомогательных функций, например 
rational_to_contfrac(x,y), 
convergents_from_contfrac(frac),
contfrac_to_rational (frac),
функций для алгоритма Миллера-Рабина,
а так же части алгоритма Винера были взяты отсюда: https://github.com/pablocelayes/rsa-wiener-attack

Идея реализации p-метода Полларда была взята из статьи https://cyberleninka.ru/article/n/realizatsiya-metoda-faktorizatsii-pollarda-na-yazyke-c

Идея реализации (p-1)-метода Полларда на языке С++ была взята отсюда https://e-maxx.ru/algo/factorization и переделана для языка python
http://window.edu.ru/catalog/pdf2txt/980/73980/53165?p_page=6

В данной реализации рассмотрены атаки:
-- методом Винера
-- p-методом Полларда
-- p-1 методом Полларда
