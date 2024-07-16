
11-07-2024 14:54

status : [[In-Progress]]

Tags: [[Machine-learning-specialization]], [[Advanced learning algorithm]] , [[Process of developing ML]]

# Building a spam classifier

Taking a text and classifying as a spam or not.

[[supervised learning]] : x = features of email , y = spam(1) or not spam(0)

Features : list the top 10,000 words of compute *X$1$,X$2$, .... , X$10,000$*

How to try to reduce your spam classifier's error ?
- collect more data. E.g., "[[Honeypot]]" project
- Develop sophisticated feature based on [[email routing]] (from email header).
- Define sophisticated features from email body. E.g., should "Discounting" and "discount" be treated as the same word.
- Design algorithms to detect misspellings. E.g., W4tches, med1cine, m0rtgage.


# References