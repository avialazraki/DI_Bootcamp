"""Week 6 Day 4 - Exercises XP: NumPy, Pandas and Linear Algebra."""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
OUTPUT = Path(__file__).resolve().parent / 'results'
OUTPUT.mkdir(exist_ok=True)

print('\nEXERCISE 1: Matrix Operations')
matrix = np.array([[4., 7., 2.], [3., 6., 1.], [2., 5., 3.]])
determinant = np.linalg.det(matrix)
print('Matrix:\n', matrix)
print('Determinant:', round(determinant, 6))
if not np.isclose(determinant, 0):
    inverse = np.linalg.inv(matrix)
    print('Inverse:\n', np.round(inverse, 4))
    print('Matrix x inverse (identity check):\n', np.round(matrix @ inverse, 4))
else:
    print('This matrix is singular; no inverse exists.')

print('\nEXERCISE 2: Statistical Analysis')
values = rng.normal(loc=50, scale=10, size=50)
print('50 random values:', np.round(values, 2))
print(f'Mean: {np.mean(values):.2f}; Median: {np.median(values):.2f}; Population standard deviation: {np.std(values):.2f}')

print('\nEXERCISE 3: Date Manipulation')
january = np.arange(np.datetime64('2023-01-01'), np.datetime64('2023-02-01'), np.timedelta64(1, 'D'))
formatted_dates = np.char.replace(january.astype(str), '-', '/')
print('January dates:', january)
print('YYYY/MM/DD:', formatted_dates)

print('\nEXERCISE 4: NumPy and Pandas Data Manipulation')
frame = pd.DataFrame(rng.integers(1, 101, size=(6, 3)), columns=['A', 'B', 'C'])
print('DataFrame:\n', frame)
print('Rows with A > 50:\n', frame.loc[frame['A'] > 50])
print('Column sums:\n', frame.sum())
print('Column means:\n', frame.mean().round(2))

print('\nEXERCISE 5: Image Representation')
print('Grayscale images use a 2D array; each value is a pixel intensity (0=black, 255=white).')
print('RGB images use a 3D array (height, width, 3) for red, green, blue channels.')
image = np.array([[0, 64, 128, 192, 255],
                  [64, 128, 192, 255, 192],
                  [128, 192, 255, 192, 128],
                  [192, 255, 192, 128, 64],
                  [255, 192, 128, 64, 0]], dtype=np.uint8)
print('5x5 grayscale image:\n', image)
fig, ax = plt.subplots(figsize=(5, 5))
ax.imshow(image, cmap='gray', vmin=0, vmax=255)
ax.set_title('5x5 Grayscale Image')
ax.set_xticks(range(5)); ax.set_yticks(range(5))
fig.tight_layout()
fig.savefig(OUTPUT / 'exercise_5_grayscale.png', dpi=160)
plt.close(fig)

print('\nEXERCISE 6: Basic Hypothesis Testing')
print('H0: Mean paired productivity improvement is <= 0.')
print('H1: Mean paired productivity improvement is > 0.')
before = rng.normal(loc=50, scale=10, size=30)
after = before + rng.normal(loc=5, scale=3, size=30)
differences = after - before
mean_difference = np.mean(differences)
sd_difference = np.std(differences, ddof=1)
t_statistic = mean_difference / (sd_difference / np.sqrt(len(differences)))
print(f'Mean before: {np.mean(before):.2f}; mean after: {np.mean(after):.2f}')
print(f'Mean improvement: {mean_difference:.2f}; paired t-statistic: {t_statistic:.3f}')
print('NumPy calculates the test statistic; a p-value requires a distribution function (e.g., SciPy).')
print('At a one-sided 5% level, compare the statistic with t critical ~1.699 for 29 degrees of freedom.')
print('Reject H0' if t_statistic > 1.699 else 'Do not reject H0')
print('This is simulated data; it does not demonstrate real-world effectiveness.')

print('\nEXERCISE 7: Element-wise Array Comparison')
first = np.array([5, 12, 7, 20, 3])
second = np.array([4, 15, 7, 10, 8])
print('First:', first, '\nSecond:', second, '\nFirst > second:', first > second)

print('\nEXERCISE 8: Time Series Slicing')
dates = pd.date_range('2023-01-01', '2023-12-31', freq='D')
series = pd.Series(rng.normal(loc=100, scale=12, size=len(dates)), index=dates, name='Value')
for label, start, end in [('January-March', '2023-01-01', '2023-03-31'),
                          ('April-June', '2023-04-01', '2023-06-30'),
                          ('July-September', '2023-07-01', '2023-09-30'),
                          ('October-December', '2023-10-01', '2023-12-31')]:
    quarter = series.loc[start:end]
    print(f'{label}: {len(quarter)} days, mean={quarter.mean():.2f}, first={quarter.index[0].date()}, last={quarter.index[-1].date()}')

print('\nEXERCISE 9: Data Conversion')
original = np.array([[1, 2, 3], [4, 5, 6]])
converted_df = pd.DataFrame(original, columns=['X', 'Y', 'Z'])
restored = converted_df.to_numpy()
print('NumPy array:\n', original)
print('Pandas DataFrame:\n', converted_df)
print('Back to NumPy:\n', restored)

print('\nEXERCISE 10: Basic Visualization')
x = np.arange(1, 21)
y = rng.integers(0, 100, size=20)
fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(x, y, marker='o', linewidth=1.8)
ax.set(title='Random Values Generated with NumPy', xlabel='Observation', ylabel='Value')
ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig(OUTPUT / 'exercise_10_line_chart.png', dpi=160)
plt.close(fig)
print('Chart saved:', OUTPUT / 'exercise_10_line_chart.png')
print('\nCompleted all 10 exercises. Charts saved in:', OUTPUT)
