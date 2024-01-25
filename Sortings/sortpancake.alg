// Блинная сортировка
// Массив данных из nof_numbers чисел, каждое из которых number_size бит.

define nof_numbers 10;
define number_size 8;

__in bit data[nof_numbers][number_size];
__out bit sorted_data[nof_numbers][number_size];

void Flip(int p)
{
	for (int i = 0; i < p; i = i + 1)
	{
		p = p - 1;
		bit tmp[number_size] = data[i];
		data[i] = data[p];
		data[p] = tmp;
	}
}

void main()
{
  	for(int i = nof_numbers - 1; i >= 0; i = i - 1)
	{
		bit max[4] = 0;
		for(int j = 1; j <= i; j = j + 1)
		{
			for(int d = 0; d <= i; d = d + 1)
			{
				if((max == d) & (data[d] < data[j]))
				{
					max = j;
				}
			}
		}
		for(int t = 1; t < i; t = t + 1)
		{
			if(max == t)
			{
				Flip(t + 1);
			}

		}
		if(max != i)
		{
			Flip(i + 1);
		}
	}
	sorted_data = data;
}

