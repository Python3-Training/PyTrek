***
## PyTrek 2020
***

The original free-and-open Star Trek console game was THE most played game of the day .... back in the 1970's! 

![PyTrek 2020](https://github.com/Python3-Training/PyTrek-2020/blob/master/PyTrek.png)

Originally written in B.A.S.I.C, from C/C++, FORTRAN, C#, Python 2 ... and now Python 3, many have been inspired to re-create, improve, and / or simply experiment with the concept.

So far:

* Converted from Python 2, to Python 3. 

* Changed in-system coordinates to simple 'chess like' (b,4 (etc)) references.

* Added random event Quips – should make the game a tad more ‘NPC’?

* Added that classic sublight / in system propulsion system. Warp speeds engines are now a seperate navigational system.

* Warp speed selection changes game time. (Thanks Loondas!)

* Heavily re-factored for growth, testing, re-use, and maintenance using modern Python.

Video: https://youtu.be/TpmtCLOJ5Uw

Original authors did an excellent job - made the modernization a WHOLE LOT easier!

Feel free to do a 'Kirk here - Kobayashi Maru?

https://www.udemy.com/course/python-1000/ 



Enjoy the journey,


-- Randall Nagy


## zSupport?
If you want to support the effort, I seek no donations. Instead, simply feel free to purchase one of [my educational](https://www.udemy.com/user/randallnagy2/) or [printed](https://www.amazon.com/Randall-Nagy/e/B08ZJLH1VN?ref=sr_ntt_srch_lnk_1&qid=1660050704&sr=8-1) productions?

Original:


================
 Star Trek 1971
================
------------
 for Python
------------

About
=====

I recently discovered the classic old BASIC game `Star Trek`_ from 1971, through a post seen on Reddit_.

The post contained a version of the game rewritten in C-Sharp which I thought was quite good.
I wondered if anyone had ported it to Python.

After a little bit of research, I didn't find a definitive version for Python.

This is by no means a definitive version itself; I just took the C# version and converted it to Python.

.. _Star Trek: http://en.wikipedia.org/wiki/Star_Trek_%28text_game%29
.. _Reddit: http://www.codeproject.com/Articles/28228/Star-Trek-Text-Game

Improvements
============

There's heaps that can be done with this program. A lot of implementations used global variables.
I tried to fix this by encapsulating them in a global object, but this can definitely be improved further.

Here is a list of possible improvements:

- Encapsulate everything in classes
- Include help/instructions
- Add extra features;
   + new ships, celestial objects, etc
   + new weapon types
   + crew functions
- Easier navigation (using cartesian system maybe)
- Make some parts more 'Pythonic'
- ...Plenty more!

