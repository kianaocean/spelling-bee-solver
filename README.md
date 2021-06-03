# spelling-bee-solver
Over my winter break, I became addicted to the daily New York Times Spelling Bee game. One afternoon, while struggling to reach Genius level (and attempting to do so by randomly entering letter combinations that I was sure were not actual English words) I started to think about how the solutions to this game could be automatically generated using the rules of the game, that day's letters, and a list of all words in the English language.

Having recently learned web scraping in my Python class, I set out to see if I could create a solver for this game.

After scraping the data from the NY Times site, I realized that embedded in the data was not only that day's letters, but also the solution words for that day's puzzle.

I was still curious how my solutions that were generated using logic and the corpus of English words matched up with the official solutions, sanctioned by editor Sam Ezersky. What I found was there were a remarkable number of "obscure, hyphenated, or proper nouns" that did not qualify as words, according to Mr. Ezersky. (This left me wondering how the NY Times goes about deciding what makes a word obscure... perhaps a project for another day :))

My main takeaway from this project: If you are addicted to a game and no longer want to be, figure out a way to cheat. That really takes the fun out of it! Needless to say I haven't played the Spelling Bee since January...

Solves NYTimes Spelling Bee puzzle using Python
1. Identifies today's hive letters and all valid answers from NYTimes site
2. Identifies any additional valid English words that meet requirements of puzzle but are not valid answers because they are "obscure, hyphenated, or proper nouns"
3. Exports text file with solutions
