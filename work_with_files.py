import math
import os


def find_files(dir, format):
    """Производит поиск файлов указанного формата в папке

    :param dir: каталог, в котором производится поиск
    :param format: формат файла
    :return: список найденных файлов
    """
    out = []
    for root, dirs, files in os.walk(dir + "\\DATA"):
        for file in files:
            if file.endswith(format):
                out.append(os.path.join(root, file))
    return out


def get_sample(filename):
    """Производит считывание выборки

    :param filename: Имя файла, в котором хранится выборка
    :return: Выборка
    """
    f = open(filename)
    sample = []
    for line in f:
        sample.append(line)
    f.close()
    return sample


def centring_value(sample):
    """Производим центрирование наблюдений относительно первого значения в выборке

    :param sample: Выборка
    :return: Центрированная выборка
    """
    first_value = float(sample[0].value)
    result = []
    sum = 0
    for obs in sample:
        obs.value = float(obs.value) - first_value
        sum += obs.value
        if math.fabs(obs.value) >= 100:
            break
        else:
            result.append(obs.value)
    return result
