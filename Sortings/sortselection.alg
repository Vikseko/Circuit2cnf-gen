// Сортировка выбором
// Массив данных из nof_numbers чисел, каждое из которых number_size бит.
// log_size массив индексов чисел (2**log_size >= nof_numbers)

define nof_numbers 10;
define log_size 4;
define number_size 8;

__in bit data[nof_numbers][number_size];
__out bit sorted_data[nof_numbers][number_size];

void main()
{
	for(int i = 0; i < nof_numbers - 1; i = i + 1)
	{
		bit min[log_size] = i;
		for(int j = i + 1; j < nof_numbers; j = j + 1)
		{
			// if(data[j] < data[min]) min = j;
			for(int k = i; k < nof_numbers; k = k + 1)
			{
				if((min == k) & (data[j] < data[k]))
				{
					min = j;
				}
			}
		}
		for(int k = i; k < nof_numbers; k = k + 1)
		{
			if(min == k)
			{
				bit t[number_size] = data[i];
				data[i] = data[k];
				data[k] = t;
			}
		}
	}
	sorted_data = data;
}
