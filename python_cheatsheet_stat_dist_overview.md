# Norm overview

- ``rvs`` = random variates (generate random samples)
- ``pdf`` = probability density function (density at each value)
- ``cdf`` = cumulative distribution function: <i>P(X≤x)</i>
- ``ppf`` = percent point function (inverse CDF / quantile)

```python
norm.rvs(loc=0, scale=1, size=None, random_state=None)
```
- ``loc``: mean
- ``scale``: standard deviation
- ``size``: number of random values to generate
- ``random_state``: seed/RandomState for reproducibility

```python
norm.pdf(x, loc=0, scale=1)
```
- ``x``: value to evaluate the density at
- ``loc``: mean
- ``scale``: standard deviation

```python
norm.cdf(x, loc=0, scale=1)
```
- same parameters as for ``pdf``, but returns <i>P(X≤x)</i>

```python
norm.ppf(q, loc=0, scale=1)
```
- ``q``: cumulative probability between 0 and 1
- ``loc``: mean
- ``scale``: standard deviation
- returns the value <i>x</i> such that <i>P(X≤x)=q</i>


# Expon overview

- **Analogy**: waiting time until the next event (e.g., minutes until the next email arrives)
- ``rvs`` = random variates (generate random samples)
- ``pdf`` = probability density function (density at each value)
- ``cdf`` = cumulative distribution function: <i>P(X≤x)</i>
- ``ppf`` = percent point function (inverse CDF / quantile)

```python
expon.rvs(loc=0, scale=1, size=None, random_state=None)
```
- ``loc``: shift/start point (usually 0)
- ``scale``: average waiting time ( = 1 / rate λ )
- ``size``: number of random values to generate
- ``random_state``: seed/RandomState for reproducibility

```python
expon.pdf(x, loc=0, scale=1)
```
- ``x``: waiting time value
- ``loc``: shift/start point
- ``scale``: average waiting time

```python
expon.cdf(x, loc=0, scale=1)
```
- same parameters as for ``pdf``, but returns <i>P(X≤x)</i>

```python
expon.ppf(q, loc=0, scale=1)
```
- ``q``: cumulative probability between 0 and 1
- ``loc``: shift/start point
- ``scale``: average waiting time
- returns the value <i>x</i> such that <i>P(X≤x)=q</i>


# Student (t) overview

- **Analogy**: estimating a true average from a **small sample** when population standard deviation is unknown (more uncertainty than Normal)
- ``rvs`` = random variates (generate random samples)
- ``pdf`` = probability density function (density at each value)
- ``cdf`` = cumulative distribution function: <i>P(X≤x)</i>
- ``ppf`` = percent point function (inverse CDF / quantile)

```python
t.rvs(df, loc=0, scale=1, size=None, random_state=None)
```
- ``df``: degrees of freedom (smaller ``df`` = heavier tails)
- ``loc``: center (mean-like location)
- ``scale``: spread
- ``size``: number of random values to generate
- ``random_state``: seed/RandomState for reproducibility

```python
t.pdf(x, df, loc=0, scale=1)
```
- ``x``: value to evaluate the density at
- ``df``: degrees of freedom
- ``loc``: center
- ``scale``: spread

```python
t.cdf(x, df, loc=0, scale=1)
```
- same parameters as for ``pdf``, but returns <i>P(X≤x)</i>

```python
t.ppf(q, df, loc=0, scale=1)
```
- ``q``: cumulative probability between 0 and 1
- ``df``: degrees of freedom
- ``loc``: center
- ``scale``: spread
- returns the value <i>x</i> such that <i>P(X≤x)=q</i>


# Lognorm overview

- **Analogy**: outcomes created by many **multiplicative** effects (e.g., incomes, house prices, file sizes) — values stay positive and are usually right-skewed
- variable whose logarithm is normally distributed
    - length of chess games
    - adult blood pressure
    - number of hospitalizations in the 2003 SARS outbreak
- ``rvs`` = random variates (generate random samples)
- ``pdf`` = probability density function (density at each value)
- ``cdf`` = cumulative distribution function: <i>P(X≤x)</i>
- ``ppf`` = percent point function (inverse CDF / quantile)

```python
lognorm.rvs(s, loc=0, scale=1, size=None, random_state=None)
```
- ``s``: shape parameter (σ of the underlying Normal in log-space)
- ``loc``: shift (usually 0)
- ``scale``: <i>e^μ</i> of the underlying Normal in log-space
- ``size``: number of random values to generate
- ``random_state``: seed/RandomState for reproducibility

```python
lognorm.pdf(x, s, loc=0, scale=1)
```
- ``x``: positive value to evaluate the density at
- ``s``: shape parameter
- ``loc``: shift
- ``scale``: <i>e^μ</i>

```python
lognorm.cdf(x, s, loc=0, scale=1)
```
- same parameters as for ``pdf``, but returns <i>P(X≤x)</i>

```python
lognorm.ppf(q, s, loc=0, scale=1)
```
- ``q``: cumulative probability between 0 and 1
- ``s``: shape parameter
- ``loc``: shift
- ``scale``: <i>e^μ</i>
- returns the value <i>x</i> such that <i>P(X≤x)=q</i>



# Binom overview

- ``rvs`` = random variates (generate random samples)
- ``pmf`` = probability mass function (exact probability for each integer <i>k</i>)
- ``cdf`` = cumulative distribution function: <i>P(X≤k)</i>


```python
binom.rvs(n, p, loc=0, size=None, random_state=None)
```
- ``n``: number of trials
- ``p``: success probability per trial
- ``loc``: shift (usually leave at 0)
- ``size``: number of random values to generate
- ``random_state``: seed/RandomState for reproducibility

```python
binom.pmf(k, n, p, loc=0)
```
- ``k``: number of successes
- ``n``: number of trials
- ``p``: success probability per trial
- ``loc``: shift (usually 0)

```python
binom.pmf(k, n, p, loc=0)
```
- same as for ``pmf``, but returns <i>P(X≤k)</i>


# Poisson overview

- **Analogy**: count how many events happen in a fixed interval (e.g., emails per hour)
- ``rvs`` = random variates (generate random samples)
- ``pmf`` = probability mass function (exact probability for each integer <i>k</i>)
- ``cdf`` = cumulative distribution function: <i>P(X≤k)</i>

```python
poisson.rvs(mu, loc=0, size=None, random_state=None)
```
- ``mu``: expected number of events in the interval (rate parameter)
- ``loc``: shift (usually leave at 0)
- ``size``: number of random values to generate
- ``random_state``: seed/RandomState for reproducibility

```python
poisson.pmf(k, mu, loc=0)
```
- ``k``: number of observed events
- ``mu``: expected number of events in the interval
- ``loc``: shift (usually 0)

```python
poisson.cdf(k, mu, loc=0)
```
- same parameters as for ``pmf``, but returns <i>P(X≤k)</i>