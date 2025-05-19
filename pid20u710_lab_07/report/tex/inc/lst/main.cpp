double multi_threads(
	std::vector<std::string> urls, // 1
	int col_threads, 			   // 2
	int tests)                     // 3
	{
	
    std::thread threads[128]; // 4

	clock_t begin = clock(); // 5
	for (int test = 0; test < tests; ++test) { // 6
		
        int index = 0; // 7
		while (index < urls.size()) { // 8

			int col_worked_threads = 0; // 9
			for (int i = 0; i < col_threads; ++i) { // 10

                if (index >= urls.size()) // 11
                    break; // 12
                
				threads[i] = std::thread(thread_func, &urls, index); // 13
                index++; // 14
                col_worked_threads++; // 15
            }

			for (int i = 0; i < col_worked_threads; ++i) // 16
				threads[i].join(); // 17
		}
	}
	
	clock_t end = clock(); // 18

	return double(end - begin) / CLOCKS_PER_SEC / tests; // 19
}