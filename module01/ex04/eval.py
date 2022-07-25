class Evaluator:
    def zip_evaluate(coefs: list, words: list):
        words = [len(word) for word in words]
        zipped = zip(words, coefs)
        return sum([w * c for w, c in zipped])

    def enumerate_evaluate(coefs: list, words: list):
        words = [len(word) for word in words]
        enum = enumerate(words)
        return sum([w * coefs[i] for i, w in enum])


if __name__ == '__main__':
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    print(Evaluator.enumerate_evaluate(coefs, words))

    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    print(Evaluator.zip_evaluate(coefs, words))
