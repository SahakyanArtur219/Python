import random
import string
import threading
import multiprocessing
import os
import time


def create_large_text_file(filename, num_sentences=1000000):
    words = [''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 8))) for _ in range(1000)]
    with open(filename, 'w') as f:
        for _ in range(num_sentences):
            sentence = ' '.join(random.choices(words, k=random.randint(5, 15)))
            f.write(sentence + '\n')


create_large_text_file('Big_file.txt')



def count_words(filename):
    word_count = {}
    with open(filename, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    return word_count




def count_words_multithreaded(filename):
    word_count = {}
    lock = threading.Lock()
    
    def process_chunk(start, end):
        local_word_count = {}
        with open(filename, 'r') as f:
            f.seek(start)
            while f.tell() < end:
                line = f.readline()
                words = line.split()
                for word in words:
                    if word in local_word_count:
                        local_word_count[word] += 1
                    else:
                        local_word_count[word] = 1
        with lock:
            for word, count in local_word_count.items():
                if word in word_count:
                    word_count[word] += count
                else:
                    word_count[word] = count

    file_size = os.path.getsize(filename)
    chunk_size = file_size // 4  # Divide file into 4 chunks
    threads = []
    for i in range(4):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < 3 else file_size
        thread = threading.Thread(target=process_chunk, args=(start, end))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return word_count





def process_chunk_multiprocess(filename, start, end):
    local_word_count = {}
    with open(filename, 'r') as f:
        f.seek(start)
        while f.tell() < end:
            line = f.readline()
            words = line.split()
            for word in words:
                
                if word in local_word_count:
                    local_word_count[word] += 1
                else:
                    local_word_count[word] = 1

    return local_word_count

def count_words_multiprocess(filename):
    file_size = os.path.getsize(filename)
    chunk_size = file_size // 4 
    pool = multiprocessing.Pool(4)
    results = []

    for i in range(4):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < 3 else file_size
        result = pool.apply_async(process_chunk_multiprocess, (filename, start, end))
        results.append(result)

    pool.close()
    pool.join()

    word_count = {}
    for result in results:
        local_word_count = result.get()
        for word, count in local_word_count.items():
            if word in word_count:
                word_count[word] += count
            else:
                word_count[word] = count

    return word_count





def measure_time(function, *args):
    start_time = time.time()
    result = function(*args)
    end_time = time.time()
    return result, end_time - start_time

if __name__ == "__main__":
    filename = 'Big_file.txt'

    _, seq_time = measure_time(count_words, filename)
    print(f"Sequential version took {seq_time:.2f} seconds")

    _, mt_time = measure_time(count_words_multithreaded, filename)
    print(f"Multithreading version took {mt_time:.2f} seconds")


    _, mp_time = measure_time(count_words_multiprocess, filename)
    print(f"Multiprocessing version took {mp_time:.2f} seconds")


    print(f"Speedup with multithreading: {seq_time / mt_time:.2f}")
    print(f"Speedup with multiprocessing: {seq_time / mp_time:.2f}")