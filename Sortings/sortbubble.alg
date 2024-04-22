// Сортировка пузырьком
// Массив данных из nof_numbers чисел, каждое из которых number_size бит.

define nof_numbers 10;
define number_size 8;

__in bit data[nof_numbers][number_size];
__out bit sorted_data[nof_numbers][number_size];

void main()
{
	for(int i = 0; i < nof_numbers - 1; i = i + 1)
	{
		for(int j = 0; j < nof_numbers - i - 1; j = j + 1)
		{
			if(data[j] > data[j + 1])
			{
				bit t[number_size] = data[j];
				data[j] = data[j+1];
				data[j+1] = t;
			}
		}
	}
	sorted_data = data;
}
