  #--  --  --  -- Statistical Thinking in Python (Part 2):
# Used for Data Scientist Training Path 
#FYI it's a compilation of how to work
#with different commands.

### --------------------------------------------------------
# ------>>>>>  How often do we get no-hitters?
# Seed random number generator
np.random.seed(42)
# Compute mean no-hitter time: tau
tau = np.mean(nohitter_times)
# Draw out of an exponential distribution with parameter tau: inter_nohitter_time
inter_nohitter_time = np.random.exponential(tau, 100000)
# Plot the PDF and label axes
plt.hist(inter_nohitter_time,
             bins=50, normed=True, histtype='step')
plt.xlabel('Games between no-hitters')
plt.ylabel('PDF')
# Show the plot
plt.show()

### --------------------------------------------------------
# ------>>>>>  Do the data follow our story?
# Create an ECDF from real data: x, y
x, y = ecdf(nohitter_times)
# Create a CDF from theoretical samples: x_theor, y_theor
x_theor, y_theor = ecdf(inter_nohitter_time)
# Overlay the plots
plt.plot(x_theor, y_theor)
plt.plot(x, y, marker='.', linestyle='none')
# Margins and axis labels
plt.margins(0.02)
plt.xlabel('Games between no-hitters')
plt.ylabel('CDF')
# Show the plot
plt.show()


### --------------------------------------------------------
# ------>>>>> How is this parameter optimal?
# Plot the theoretical CDFs
plt.plot(x_theor, y_theor)
plt.plot(x, y, marker='.', linestyle='none')
plt.margins(0.02)
plt.xlabel('Games between no-hitters')
plt.ylabel('CDF')
# Take samples with half tau: samples_half
samples_half = np.random.exponential(tau/2,10000)
# Take samples with double tau: samples_double
samples_double = np.random.exponential(tau*2,10000)
# Generate CDFs from these samples
x_half, y_half = ecdf(samples_half)
x_double, y_double = ecdf(samples_double)
# Plot these CDFs as lines
plt.plot(x_half, y_half)
plt.plot(x_double, y_double)
# Show the plot
plt.show()


### --------------------------------------------------------
# ------>>>>> EDA of literacy/fertility data
# Plot the illiteracy rate versus fertility
plt.plot(illiteracy, fertility, marker='.', linestyle='none')
# Set the margins and label axes
plt.margins(0.02)
plt.xlabel('percent illiterate')
plt.ylabel('fertility')
# Show the plot
plt.show()
# Show the Pearson correlation coefficient
print(pearson_r(illiteracy, fertility))


### --------------------------------------------------------
# ------>>>>>Linear regression
# Plot the illiteracy rate versus fertility
plt.plot(illiteracy, fertility, marker='.', linestyle='none')
plt.margins(0.02)
plt.xlabel('percent illiterate')
plt.ylabel('fertility')
# Perform a linear regression using np.polyfit(): a, b
a, b = np.polyfit(illiteracy, fertility, 1)
# Print the results to the screen
print('slope =', a, 'children per woman / percent illiterate')
print('intercept =', b, 'children per woman')
# Make theoretical line to plot
x = np.array([0, 100])
y = a * x + b
# Add regression line to your plot
plt.plot(x, y)
# Draw the plot
plt.show()


### --------------------------------------------------------
# ------>>>>>How is it optimal?
# Specify slopes to consider: a_vals
a_vals = np.linspace(0, 0.1, 200)
# Initialize sum of square of residuals: rss
rss = np.empty_like(a_vals)
# Compute sum of square of residuals for each value of a_vals
for i, a in enumerate(a_vals):
    rss[i] = np.sum((fertility - a*illiteracy - b)**2)
# Plot the RSS
plt.plot(a_vals, rss, '-')
plt.xlabel('slope (children per woman / percent illiterate)')
plt.ylabel('sum of square of residuals')
plt.show()

### --------------------------------------------------------
# ------>>>>>The importance of EDA - exploratory data analysis
# Why should exploratory data analysis be the first 
# step in an analysis of data (after getting your data 
# imported and cleaned, of course.
# R/ ---> All of these reasons!
#You can be protected from misinterpretation of the type demonstrated by Anscombe's quartet.
#EDA provides a good starting point for planning the rest of your analysis.
#EDA is not really any more difficult than any of the subsequent analysis, so 
#there is no excuse for not exploring the data.

### --------------------------------------------------------
# ------>>>>> Linear regression on appropriate Anscombe data
# Perform linear regression: a, b
a, b = np.polyfit(x, y, 1)
# Print the slope and intercept
print(a, b)
# Generate theoretical x and y data: x_theor, y_theor
x_theor = np.array([3, 15])
y_theor = a * x_theor + b
# Plot the Anscombe data and theoretical line
plt.plot(x, y, marker='.', linestyle='none')
plt.plot(x_theor, y_theor)
# Label the axes
plt.xlabel('x')
plt.ylabel('y')
# Show the plot
plt.show()


### --------------------------------------------------------
# ------>>>>> Linear regression on all Anscombe data
# Iterate through x,y pairs
for x, y in zip(anscombe_x, anscombe_y):
    # Compute the slope and intercept: a, b
    a, b = np.polyfit(x, y, 1)
    # Print the result
    print('slope:', a, 'intercept:', b)



### --------------------------------------------------------
# ------>>>>>Getting the terminology down
# Getting tripped up over terminology is a common cause of 
# frustration in students. Unfortunately, you often will read 
# and hear other data scientists using different terminology 
# for bootstrap samples and replicates. This is even more reason 
# why we need everything to be clear and consistent for this 
# course. So, before going forward discussing bootstrapping, 
# let's get our terminology down. If we have a data set with 
# repeated measurements, a bootstrap sample is an array of 
# length  that was drawn from the original data with replacement.
# What is a bootstrap replicate?
# R/ A single value of a statistic computed from a bootstrap sample.


### --------------------------------------------------------
# ------>>>>> Bootstrapping by hand
# To help you gain intuition about how bootstrapping works, 
# imagine you have a data set that has only three points, 
# [-1, 0, 1]. How many unique bootstrap samples can be drawn 
# (e.g., [-1, 0, 1] and [1, 0, -1] are unique), and what 
# is the maximum mean you can get from a bootstrap sample? 
# It might be useful to jot down the samples on a piece of paper.
# (These are too few data to get meaningful results from bootstrap 
# procedures, but this example is useful for intuition.)
# R/ There are 27 unique samples, and the maximum mean is 1.




### --------------------------------------------------------
# ------>>>>> Visualizing bootstrap samples
for _ in range(50):
    # Generate bootstrap sample: bs_sample
    bs_sample = np.random.choice(rainfall, size=len(rainfall))
    # Compute and plot ECDF from bootstrap sample
    x, y = ecdf(bs_sample)
    plt.plot(x, y, marker='.', linestyle='none',
                 color='gray', alpha=0.1)
# Compute and plot ECDF from original data
x, y = ecdf(rainfall)
plt.plot(x, y, marker='.')
# Make margins and label axes
plt.margins(0.02)
plt.xlabel('yearly rainfall (mm)')
plt.ylabel('ECDF')
# Show the plot
plt.show()



### --------------------------------------------------------
# ------>>>>> Generating many bootstrap replicates
def draw_bs_reps(data, func, size=1):
    """Draw bootstrap replicates."""
    # Initialize array of replicates: bs_replicates
    bs_replicates = np.empty(size)
    # Generate replicates
    for i in range(size):
        bs_replicates[i] = bootstrap_replicate_1d(data, func)
    return bs_replicates



### --------------------------------------------------------
# ------>>>>> Bootstrap replicates of the mean and the SEM
# Take 10,000 bootstrap replicates of the mean: bs_replicates
bs_replicates = draw_bs_reps(rainfall, np.mean, size=10000)
# Compute and print SEM
sem = np.std(rainfall) / np.sqrt(len(rainfall))
print(sem)
# Compute and print standard deviation of bootstrap replicates
bs_std = np.std(bs_replicates)
print(bs_std)
# Make a histogram of the results
plt.hist(bs_replicates, bins=50, normed=True)
plt.xlabel('mean annual rainfall (mm)')
plt.ylabel('PDF')
# Show the plot
plt.show()



### --------------------------------------------------------
# ------>>>>> Confidence intervals of rainfall data
# A confidence interval gives upper and lower bounds on the range
#  of parameter values you might expect to get if we repeat our 
# measurements. For named distributions, you can compute them 
# analytically or look them up, but one of the many beautiful 
# properties of the bootstrap method is that you can take 
# percentiles of your bootstrap replicates to get your confidence 
# interval. Conveniently, you can use the np.percentile() function.
# Use the bootstrap replicates you just generated to compute the 95% 
# confidence interval. That is, give the 2.5th and 97.5th percentile 
# of your bootstrap replicates stored as bs_replicates. What is 
# the 95% confidence interval?
conf_int = np.percentile(bs_replicates, [2.5, 97.5])
print(conf_int)
#R/ (780, 821) mm/year





### --------------------------------------------------------
# ------>>>>> Bootstrap replicates of other statistics
# Generate 10,000 bootstrap replicates of the variance: bs_replicates
bs_replicates = draw_bs_reps(rainfall, np.var, size=10000)
# Put the variance in units of square centimeters
bs_replicates /= 100
# Make a histogram of the results
plt.hist(bs_replicates, normed=True, bins=50)
plt.xlabel('variance of annual rainfall (sq. cm)')
plt.ylabel('PDF')
# Show the plot
plt.show()



### --------------------------------------------------------
# ------>>>>>Confidence interval on the rate of no-hitters
# Draw bootstrap replicates of the mean no-hitter time (equal to tau): bs_replicates
bs_replicates = draw_bs_reps(nohitter_times, np.mean, size=10000)
# Compute the 95% confidence interval: conf_int
conf_int = np.percentile(bs_replicates, [2.5, 97.5])
# Print the confidence interval
print('95% confidence interval =', conf_int, 'games')
# Plot the histogram of the replicates
plt.hist(bs_replicates, bins=50, normed=True)
plt.xlabel(r'$\tau$ (games)')
plt.ylabel('PDF')
# Show the plot
plt.show()



### --------------------------------------------------------
# ------>>>>> A function to do pairs bootstrap
def draw_bs_pairs_linreg(x, y, size=1):
    """Perform pairs bootstrap for linear regression."""
    # Set up array of indices to sample from: inds
    inds = np.arange(len(x))
    # Initialize replicates: bs_slope_reps, bs_intercept_reps
    bs_slope_reps = np.empty(size)
    bs_intercept_reps = np.empty(size)
    # Generate replicates
    for i in range(size):
        bs_inds = np.random.choice(inds, size=len(inds))
        bs_x, bs_y = x[bs_inds], y[bs_inds]
        bs_slope_reps[i], bs_intercept_reps[i] = np.polyfit(bs_x, bs_y, 1)
    return bs_slope_reps, bs_intercept_reps



### --------------------------------------------------------
# ------>>>>> Pairs bootstrap of literacy/fertility data
# Generate replicates of slope and intercept using pairs bootstrap
bs_slope_reps, bs_intercept_reps = draw_bs_pairs_linreg(
                    illiteracy, fertility, size=1000)
# Compute and print 95% CI for slope
print(np.percentile(bs_slope_reps, [2.5, 97.5]))
# Plot the histogram
plt.hist(bs_slope_reps, bins=50, normed=True)
plt.xlabel('slope')
plt.ylabel('PDF')
plt.show()




### --------------------------------------------------------
# ------>>>>> Plotting bootstrap regressions
# Generate array of x-values for bootstrap lines: x
x = np.array([0, 100])
# Plot the bootstrap lines
for i in range(100):
    plt.plot(x, bs_slope_reps[i] * x + bs_intercept_reps[i],
                 linewidth=0.5, alpha=0.2, color='red')
# Plot the data
plt.plot(illiteracy, fertility, marker='.', linestyle='none')
# Label axes, set the margins, and show the plot
plt.xlabel('illiteracy')
plt.ylabel('fertility')
plt.margins(0.02)
plt.show()




### --------------------------------------------------------
# ------>>>>> Generating a permutation sample
def permutation_sample(data1, data2):
    """Generate a permutation sample from two data sets."""
    # Concatenate the data sets: data
    data = np.concatenate((data1, data2))
    # Permute the concatenated array: permuted_data
    permuted_data = np.random.permutation(data)
    # Split the permuted array into two: perm_sample_1, perm_sample_2
    perm_sample_1 = permuted_data[:len(data1)]
    perm_sample_2 = permuted_data[len(data1):]
    return perm_sample_1, perm_sample_2




### --------------------------------------------------------
# ------>>>>> Visualizing permutation sampling
for _ in range(50):
    # Generate permutation samples
    perm_sample_1, perm_sample_2 = permutation_sample(
                                    rain_june, rain_november)
    # Compute ECDFs
    x_1, y_1 = ecdf(perm_sample_1)
    x_2, y_2 = ecdf(perm_sample_2)
    # Plot ECDFs of permutation sample
    plt.plot(x_1, y_1, marker='.', linestyle='none',
                 color='red', alpha=0.02)
    plt.plot(x_2, y_2, marker='.', linestyle='none',
                 color='blue', alpha=0.02)
# Create and plot ECDFs from original data
x_1, y_1 = ecdf(rain_june)
x_2, y_2 = ecdf(rain_november)
plt.plot(x_1, y_1, marker='.', linestyle='none', color='red')
plt.plot(x_2, y_2, marker='.', linestyle='none', color='blue')
# Label axes, set margin, and show plot
plt.margins(0.02)
plt.xlabel('monthly rainfall (mm)')
plt.ylabel('ECDF')
plt.show()



### --------------------------------------------------------
# ------>>>>>Test statistics
# When performing hypothesis tests, your choice of test statistic should be:
# R/ be pertinent to the question you are seeking to answer in your hypothesis test.


### --------------------------------------------------------
# ------>>>>> What is a p-value?
# R/ the probability of observing a test statistic equally or 
# more extreme than the one you observed, given that the null hypothesis is true.



### --------------------------------------------------------
# ------>>>>> Generating permutation replicates
def draw_perm_reps(data_1, data_2, func, size=1):
    """Generate multiple permutation replicates."""
    # Initialize array of replicates: perm_replicates
    perm_replicates = np.empty(size)
    for i in range(size):
        # Generate permutation sample
        perm_sample_1, perm_sample_2 = permutation_sample(data_1, data_2)
        # Compute the test statistic
        perm_replicates[i] = func(perm_sample_1, perm_sample_2)
    return perm_replicates





### --------------------------------------------------------
# ------>>>>> Look before you leap: EDA before hypothesis testing
# Make bee swarm plot
sns.swarmplot(x='ID', y='impact_force', data=df)
# Label axes
plt.xlabel('frog')
plt.ylabel('impact force (N)')
# Show the plot
plt.show()




### --------------------------------------------------------
# ------>>>>> Permutation test on frog data
def diff_of_means(data_1, data_2):
    """Difference in means of two arrays."""
    # The difference of means of data_1, data_2: diff
    diff = np.mean(data_1) - np.mean(data_2)
    return diff
# Compute difference of mean impact force from experiment: empirical_diff_means
empirical_diff_means = diff_of_means(force_a, force_b)
# Draw 10,000 permutation replicates: perm_replicates
perm_replicates = draw_perm_reps(force_a, force_b,diff_of_means, size=10000)
# Compute p-value: p
p = np.sum(perm_replicates >= empirical_diff_means) / len(perm_replicates)
# Print the result
print('p-value =', p)




### --------------------------------------------------------
# ------>>>>>A one-sample bootstrap hypothesis test
# Make an array of translated impact forces: translated_force_b
translated_force_b = force_b - np.mean(force_b) + 0.55
# Take bootstrap replicates of Frog B's translated impact forces: bs_replicates
bs_replicates = draw_bs_reps(translated_force_b, np.mean, 10000)
# Compute fraction of replicates that are less than the observed Frog B force: p
p = np.sum(bs_replicates <= np.mean(force_b)) / 10000
# Print the p-value
print('p = ', p)




### --------------------------------------------------------
# ------>>>>> A two-sample bootstrap hypothesis test for difference of means
# Compute mean of all forces: mean_force
mean_force = np.mean(forces_concat)
# Generate shifted arrays
force_a_shifted = force_a - np.mean(force_a) + mean_force
force_b_shifted = force_b - np.mean(force_b) + mean_force
# Compute 10,000 bootstrap replicates from shifted arrays
bs_replicates_a = draw_bs_reps(force_a_shifted, np.mean, size=10000)
bs_replicates_b = draw_bs_reps(force_b_shifted, np.mean, size=10000)
# Get replicates of difference of means: bs_replicates
bs_replicates = bs_replicates_a - bs_replicates_b
# Compute and print p-value: p
p = np.sum(bs_replicates >= empirical_diff_means) / len(bs_replicates)
print('p-value =', p)




### --------------------------------------------------------
# ------>>>>> The vote for the Civil Rights Act in 1964
# Construct arrays of data: dems, reps
dems = np.array([True] * 153 + [False] * 91)
reps = np.array([True] * 136 + [False] * 35)
def frac_yea_dems(dems, reps):
    """Compute fraction of Democrat yea votes."""
    frac = np.sum(dems) / len(dems)
    return frac
# Acquire permutation samples: perm_replicates
perm_replicates = draw_perm_reps(dems, reps, frac_yea_dems, size=10000)
# Compute and print p-value: p
p = np.sum(perm_replicates <= 153/244) / len(perm_replicates)
print('p-value =', p)




### --------------------------------------------------------
# ------>>>>> What is equivalent?
# You have experience matching stories to probability distributions.
#  Similarly, you use the same procedure for two different A/B tests 
# if their stories match. In the Civil Rights Act example you just did, 
# you performed an A/B test on voting data, which has a Yes/No type of 
# outcome for each subject (in that case, a voter). Which of the following 
# situations involving testing by a web-based company has an equivalent 
# set up for an A/B test as the one you just did with the Civil Rights
#  Act of 1964?
# R/ You measure the number of people who click on an ad on your
#  company's website before and after changing its color.



### --------------------------------------------------------
# ------>>>>> A time-on-website analog
# Compute the observed difference in mean inter-no-hitter times: nht_diff_obs
nht_diff_obs = diff_of_means(nht_dead, nht_live)
# Acquire 10,000 permutation replicates of difference in mean no-hitter time: perm_replicates
perm_replicates = draw_perm_reps(nht_dead, nht_live,
diff_of_means, size=10000)
# Compute and print the p-value: p
p = np.sum(perm_replicates <= nht_diff_obs) / len(perm_replicates)
print('p-val =',p)




### --------------------------------------------------------
# ------>>>>> What should you have done first?
# That was a nice hypothesis test you just did to check out 
# whether the rule changes in 1920 changed the rate of no-hitters.
#  But what should you have done with the data first?
# R/ Performed EDA, perhaps plotting the ECDFs of inter-no-hitter 
# times in the dead ball and live ball eras.



### --------------------------------------------------------
# ------>>>>> Simulating a null hypothesis concerning correlation
# R/ Do a permutation test: Permute the illiteracy values but leave
#  the fertility values fixed to generate a new set of 
# (illiteracy, fertility) data.



### --------------------------------------------------------
# ------>>>>> Hypothesis test on Pearson correlation
# Compute observed correlation: r_obs
r_obs = pearson_r(illiteracy, fertility)
# Initialize permutation replicates: perm_replicates
perm_replicates = np.empty(10000)
# Draw replicates
for i in range(10000):
    # Permute illiteracy measurments: illiteracy_permuted
    illiteracy_permuted = np.random.permutation(illiteracy)
    # Compute Pearson correlation
    perm_replicates[i] = pearson_r(illiteracy_permuted, fertility)
# Compute p-value: p
p = np.sum(perm_replicates >= r_obs) / len(perm_replicates)
print('p-val =', p)



### --------------------------------------------------------
# ------>>>>> Do neonicotinoid insecticides have unintended consequences?
# Compute x,y values for ECDFs
x_control, y_control = ecdf(control)
x_treated, y_treated = ecdf(treated)
# Plot the ECDFs
plt.plot(x_control, y_control, marker='.', linestyle='none')
plt.plot(x_treated, y_treated, marker='.', linestyle='none')
# Set the margins
plt.margins(0.02)
# Add a legend
plt.legend(('control', 'treated'), loc='lower right')
# Label axes and show plot
plt.xlabel('millions of alive sperm per mL')
plt.ylabel('ECDF')
plt.show()



### --------------------------------------------------------
# ------>>>>> Bootstrap hypothesis test on bee sperm counts
# Compute the difference in mean sperm count: diff_means
diff_means = np.mean(control) - np.mean(treated)
# Compute mean of pooled data: mean_count
mean_count = np.mean(np.concatenate((control, treated)))
# Generate shifted data sets
control_shifted = control - np.mean(control) + mean_count
treated_shifted = treated - np.mean(treated) + mean_count
# Generate bootstrap replicates
bs_reps_control = draw_bs_reps(control_shifted,
                               np.mean, size=10000)
bs_reps_treated = draw_bs_reps(treated_shifted,
                               np.mean, size=10000)
# Get replicates of difference of means: bs_replicates
bs_replicates = bs_reps_control - bs_reps_treated
# Compute and print p-value: p
p = np.sum(bs_replicates >= np.mean(control) - np.mean(treated)) \
            / len(bs_replicates)
print('p-value =', p)



### --------------------------------------------------------
# ------>>>>> EDA of beak depths of Darwin's finches
# Create bee swarm plot
sns.swarmplot(data=df, x='year', y='beak_depth')
# Label the axes
plt.xlabel('year')
plt.ylabel('beak depth (mm)')
# Show the plot
plt.show()



### --------------------------------------------------------
# ------>>>>> ECDFs of beak depths
# Compute ECDFs
x_1975, y_1975 = ecdf(bd_1975)
x_2012, y_2012 = ecdf(bd_2012)
# Plot the ECDFs
plt.plot(x_1975, y_1975, marker='.', linestyle='none')
plt.plot(x_2012, y_2012, marker='.', linestyle='none')
# Set margins
plt.margins(0.02)
# Add axis labels and legend
plt.xlabel('beak depth (mm)')
plt.ylabel('ECDF')
plt.legend(('1975', '2012'), loc='lower right')
# Show the plot
plt.show()




### --------------------------------------------------------
# ------>>>>> Parameter estimates of beak depths
# Compute the difference of the sample means: mean_diff
mean_diff = np.mean(bd_2012) - np.mean(bd_1975)
# Get bootstrap replicates of means
bs_replicates_1975 = draw_bs_reps(bd_1975, np.mean, 10000)
bs_replicates_2012 = draw_bs_reps(bd_2012, np.mean, 10000)
# Compute sample of difference of means: bs_diff_replicates
bs_diff_replicates = bs_replicates_2012 - bs_replicates_1975
# Compute 95% confidence interval: conf_int
conf_int = np.percentile(bs_diff_replicates, [2.5, 97.5])
# Print the results
print('difference of means =', mean_diff, 'mm')
print('95% confidence interval =', conf_int, 'mm')





### --------------------------------------------------------
# ------>>>>> Hypothesis test: Are beaks deeper in 2012?
# Compute mean of combined data set: combined_mean
combined_mean = np.mean(np.concatenate((bd_1975, bd_2012)))
# Shift the samples
bd_1975_shifted = bd_1975 - np.mean(bd_1975) + combined_mean
bd_2012_shifted = bd_2012 - np.mean(bd_2012) + combined_mean
# Get bootstrap replicates of shifted data sets
bs_replicates_1975 = draw_bs_reps(bd_1975_shifted, np.mean, 10000)
bs_replicates_2012 = draw_bs_reps(bd_2012_shifted, np.mean, 10000)
# Compute replicates of difference of means: bs_diff_replicates
bs_diff_replicates = bs_replicates_2012 - bs_replicates_1975
# Compute the p-value: p
p = np.sum(bs_diff_replicates >= mean_diff) / len(bs_diff_replicates)
# Print p-value
print('p =', p)



### --------------------------------------------------------
# ------>>>>> EDA of beak length and depth
# Make scatter plot of 1975 data
plt.plot(bl_1975, bd_1975, marker='.',
linestyle='none', color='blue', alpha=0.5)
# Make scatter plot of 2012 data
plt.plot(bl_2012, bd_2012, marker='.',
linestyle='none', color='red', alpha=0.5)
# Label axes and make legend
plt.xlabel('beak length (mm)')
plt.ylabel('beak depth (mm)')
plt.legend(('1975', '2012'), loc='upper left')
# Show the plot
plt.show()



### --------------------------------------------------------
# ------>>>>> Linear regressions
# Compute the linear regressions
slope_1975, intercept_1975 = np.polyfit(bl_1975, bd_1975, 1)
slope_2012, intercept_2012 = np.polyfit(bl_2012, bd_2012, 1)
# Perform pairs bootstrap for the linear regressions
bs_slope_reps_1975, bs_intercept_reps_1975 = draw_bs_pairs_linreg(bl_1975, bd_1975, 1000)
bs_slope_reps_2012, bs_intercept_reps_2012 = draw_bs_pairs_linreg(bl_2012, bd_2012, 1000)
# Compute confidence intervals of slopes
slope_conf_int_1975 = np.percentile(bs_slope_reps_1975, [2.5, 97.5])
slope_conf_int_2012 = np.percentile(bs_slope_reps_2012, [2.5, 97.5])
intercept_conf_int_1975 = np.percentile(bs_intercept_reps_1975, [2.5, 97.5])
intercept_conf_int_2012 = np.percentile(bs_intercept_reps_2012, [2.5, 97.5])
# Print the results
print('1975: slope =', slope_1975,'conf int =', slope_conf_int_1975)
print('1975: intercept =', intercept_1975,'conf int =', intercept_conf_int_1975)
print('2012: slope =', slope_2012,'conf int =', slope_conf_int_2012)
print('2012: intercept =', intercept_2012,'conf int =', intercept_conf_int_2012)


### --------------------------------------------------------
# ------>>>>> Displaying the linear regression results
# Make scatter plot of 1975 data
plt.plot(bl_1975, bd_1975, marker='.',linestyle='none', color='blue', alpha=0.5)
# Make scatter plot of 2012 data
plt.plot(bl_2012, bd_2012, marker='.',linestyle='none', color='red', alpha=0.5)
# Label axes and make legend
plt.xlabel('beak length (mm)')
plt.ylabel('beak depth (mm)')
plt.legend(('1975', '2012'), loc='upper left')
# Generate x-values for bootstrap lines: x
x = np.array([10, 17])
# Plot the bootstrap lines
for i in range(100):
    plt.plot(x, bs_slope_reps_1975[i] * x + bs_intercept_reps_1975[i],linewidth=0.5, alpha=0.2, color='blue')
    plt.plot(x, bs_slope_reps_2012[i] * x + bs_intercept_reps_2012[i],linewidth=0.5, alpha=0.2, color='red')
# Draw the plot again
plt.show()


### --------------------------------------------------------
# ------>>>>> Beak length to depth ratio
# Compute length-to-depth ratios
ratio_1975 = bl_1975 / bd_1975
ratio_2012 = bl_2012 / bd_2012
# Compute means
mean_ratio_1975 = np.mean(ratio_1975)
mean_ratio_2012 = np.mean(ratio_2012)
# Generate bootstrap replicates of the means
bs_replicates_1975 = draw_bs_reps(ratio_1975, np.mean, size=10000)
bs_replicates_2012 = draw_bs_reps(ratio_2012, np.mean, size=10000)
# Compute the 99% confidence intervals
conf_int_1975 = np.percentile(bs_replicates_1975, [0.5, 99.5])
conf_int_2012 = np.percentile(bs_replicates_2012, [0.5, 99.5])
# Print the results
print('1975: mean ratio =', mean_ratio_1975,'conf int =', conf_int_1975)
print('2012: mean ratio =', mean_ratio_2012,'conf int =', conf_int_2012)


### --------------------------------------------------------
# ------>>>>> How different is the ratio?
# In the previous exercise, you computed the mean beak length
#  to depth ratio with 99% confidence intervals for 1975 and 
# for 2012. The results of that calculation are shown graphically 
# in the plot accompanying this problem. In addition to these 
# results, what would you say about the ratio of beak length
#  to depth?
# R/ The mean beak length-to-depth ratio decreased by about 
# 0.1, or 7%, from 1975 to 2012. The 99% confidence intervals 
# are not even close to overlapping, so this is a real change. 
# The beak shape changed.

### --------------------------------------------------------
# ------>>>>> EDA of heritability
# Make scatter plots
plt.plot(bd_parent_fortis, bd_offspring_fortis,marker='.', linestyle='none', color='blue', alpha=0.5)
plt.plot(bd_parent_scandens, bd_offspring_scandens,marker='.', linestyle='none', color='red', alpha=0.5)
# Set margins, make legend, label axes, and show plot
plt.margins(0.02)
# Label axes
plt.xlabel('parental beak depth (mm)')
plt.ylabel('offspring beak depth (mm)')
# Add legend
plt.legend(('G. fortis', 'G. scandens'), loc='lower right')
# Show plot
plt.show()


### --------------------------------------------------------
# ------>>>>> Correlation of offspring and parental data
def draw_bs_pairs(x, y, func, size=1):
    """Perform pairs bootstrap for single statistic."""
    # Set up array of indices to sample from: inds
    inds = np.arange(len(x))
    # Initialize replicates: bs_replicates
    bs_replicates = np.empty(size)
    # Generate replicates
    for i in range(size):
        bs_inds = np.random.choice(inds, len(inds))
        bs_x, bs_y = x[bs_inds], y[bs_inds]
        bs_replicates[i] = func(bs_x, bs_y)
    return bs_replicates


### --------------------------------------------------------
# ------>>>>> Pearson correlation of offspring and parental data
# Compute the Pearson correlation coefficients
r_scandens = pearson_r(bd_parent_scandens, bd_offspring_scandens)
r_fortis = pearson_r(bd_parent_fortis, bd_offspring_fortis)
# Acquire 1000 bootstrap replicates of Pearson r
bs_replicates_scandens = draw_bs_pairs(bd_parent_scandens, bd_offspring_scandens, pearson_r, size=1000)
bs_replicates_fortis = draw_bs_pairs(bd_parent_fortis, bd_offspring_fortis, pearson_r, size=1000)
# Compute 95% confidence intervals
conf_int_scandens = np.percentile(bs_replicates_scandens, [2.5, 97.5])
conf_int_fortis = np.percentile(bs_replicates_fortis, [2.5, 97.5])
# Print results
print('G. scandens:', r_scandens, conf_int_scandens)
print('G. fortis:', r_fortis, conf_int_fortis)


### --------------------------------------------------------
# ------>>>>> Measuring heritability
def heritability(parents, offspring):
    """Compute the heritability from parent and offspring samples."""
    covariance_matrix = np.cov(parents, offspring)
    return covariance_matrix[0,1] / covariance_matrix[0,0]
# Compute the heritability
heritability_scandens = heritability(bd_parent_scandens,bd_offspring_scandens)
heritability_fortis = heritability(bd_parent_fortis,bd_offspring_fortis)
# Acquire 1000 bootstrap replicates of heritability
replicates_scandens = draw_bs_pairs(bd_parent_scandens, bd_offspring_scandens, heritability, size=1000)
replicates_fortis = draw_bs_pairs(bd_parent_fortis, bd_offspring_fortis, heritability, size=1000)
# Compute 95% confidence intervals
conf_int_scandens = np.percentile(replicates_scandens, [2.5, 97.5])
conf_int_fortis = np.percentile(replicates_fortis, [2.5, 97.5])
# Print results
print('G. scandens:', heritability_scandens, conf_int_scandens)
print('G. fortis:', heritability_fortis, conf_int_fortis)


### --------------------------------------------------------
# ------>>>>> Is beak depth heritable at all in G. scandens?
# Initialize array of replicates: perm_replicates
perm_replicates = np.empty(10000)
# Draw replicates
for i in range(10000):
    # Permute parent beak depths
    bd_parent_permuted = np.random.permutation(bd_parent_scandens)
    perm_replicates[i] = heritability(bd_parent_permuted,bd_offspring_scandens)
# Compute p-value: p
p = np.sum(perm_replicates >= heritability_scandens) / len(perm_replicates)
# Print the p-value
print('p-val =', p)
