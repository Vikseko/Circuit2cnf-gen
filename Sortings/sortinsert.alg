// Сортировка вставками
// Массив данных из nof_numbers чисел, каждое из которых number_size бит.
// log_size массив индексов чисел (2**log_size >= nof_numbers)

define nof_numbers 10;
define log_size 4;
define number_size 8;

__in bit data[nof_numbers][number_size];
__out bit sorted_data[nof_numbers][number_size];

void main()
{
	for(int i = 1; i < nof_numbers; i = i + 1)
	{
		bit item[number_size] = data[i];
		bit cond = 1;
		bit index[log_size] = i;
		for(int j = i; j > 0; j = j - 1)
		{
			cond = cond & (data[j - 1] > item);
			if(cond)
			{
				data[j] = data[j - 1];
				index = j - 1;
			}
		}
		for(int k = 0; k < i; k = k + 1)
		{
			if(index == k)
			{
				data[k] = item;
			}
		}
	}
	sorted_data = data;
}

