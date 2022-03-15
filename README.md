Python autoclicker for left or right doubleclicks with adjustable random wait intervals.

## Usage

Left click example: 
```python
python3 autoclicker.py left --min_wait 0.1 --max_wait 5.75 --total_clicks 100
```

Right click example: 
```python
python3 autoclicker.py right --min_wait 0.1 --max_wait 5.75 --total_clicks 100
```
  
Function arguments:

- `left_or_right`
    - left or right double click
    - required
    - string
- `min_wait`
    - the minimum amount of time to wait before clicking
    - optional
    - float
    - defaults to 0
- `max_wait`
    - the maximum amount of time to wait before clicking
    - optional
    - float
    - defaults to 0
- `total_clicks`
    - how many times to click
    - optional
    - int
    - defaults to 1,000,000


