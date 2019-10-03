# Classification of the comments concerning a movie

import keras

(x_train, y_train), (x_test, y_test) = keras.datasets.imdb.load_data(path="imdb.npz",
                                                                     num_words=None,
                                                                     skip_top=0,
                                                                     maxlen=100,
                                                                     seed=113,
                                                                     start_char=1,
                                                                     oov_char=2,
                                                                     index_from=3)

