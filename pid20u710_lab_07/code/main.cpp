double multi_threads(std::vector<std::string> urls, int col_threads, int tests) {
	
    std::thread threads[128]; // 1

	clock_t begin = clock(); // 2
	for (int test = 0; test < tests; ++test) { // 3
		
        int index = 0; // 4
		while (index < urls.size()) { // 5

			int col_worked_threads = 0; // 6
			for (int i = 0; i < col_threads; ++i) { // 7

                if (index >= urls.size()) // 8
                    break; // 9
                
				threads[i] = std::thread(thread_func, &urls, index); // 10
                index++; // 11
                col_worked_threads++; // 12
            }

			for (int i = 0; i < col_worked_threads; ++i) // 13
				threads[i].join(); // 14
		}
	}
	
	clock_t end = clock(); // 15

	return double(end - begin) / CLOCKS_PER_SEC / tests; // 16
}