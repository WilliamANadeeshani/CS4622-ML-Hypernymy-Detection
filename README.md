CS4622 - ML - Group 11 - Hypernymy Detection for travel Domain

1. we've focused on the common hypernym relation between nouns (and noun phrases).
2. We developed a method that given a pair of nouns (x, y) (e.g. (cat, animal)) predicts whether y is a hypernym of x - or in other words, whether x is a subclass of y (e.g. cats are a subclass of animals) or an instance of y (e.g. abbey road is an instance of record).
3. we combined the complementary path-based and distributional approaches. 
4. To add distributional information to our model (the information on the separate occurrences of each term x and y), we simply added the word embedding vectors of x and y to the model, allowing it to rely on this information as well. 
5. With this simple change we achieve significant improvement in performance compared to prior methods in each approach.

