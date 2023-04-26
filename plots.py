import numpy as np
import matplotlib.pyplot as plt

# Data
networks = ['TANN', 'SIREN', 'PWNN']
layers_units = [1, 2, 3, 4]
units = [5,10,20]
values_ours = {
    'TANN': {
        5: [1.5e-3,3.7e-4,7.4e-2,5.3e-4],
        10: [1.0e-3,8.6e-4,4.7e-4,1.0e-3],
        20: [3.4e-1,3.3e-1,1.3e-3,5.3e-4]
    },
    'SIREN': {
        5: [4.2e-4,5.1e-4,6.9e-4,3.5e-4],
        10: [5.7e-4,5.1e-4,3.8e-4,3.1e-4],
        20: [1.0e-3,7.7e-4,5.7e-4,8.7e-4]
    },
    'PWNN': {
        5: [1.7e-4, 5.5e-5, 2.2e-4, 2.2e-5],
        10: [1.6e-4, 3.4e-5, 2.4e-4, 1.9e-5],
        20: [1.4e-4, 1.9e-5, 3.0e-4, 2.2e-5]
    }
}
values_paper = {
    'TANN': {
        5: [1.8e-1,9.5e-2,2.0e-2,1.6e-2],
        10: [8.2e-3,3.4e-3,2.3e-3,2.8e-3],
        20: [4.5e-3,1.8e-3,2.0e-3,3.0e-3]
    },
    'SIREN': {
        5: [8.5e-2,1.4e-2,6.9e-3,5.6e-3],
        10: [6.5e-3,1.7e-3,3.0e-3,2.0e-3],
        20: [8.2e-3,3.2e-3,1.7e-3,1.1e-3]
    },
    'PWNN': {
        5: [1.8e-1,1.8e-3,2.8e-3,1.8e-3],
        10: [4.1e-4,4.7e-4,2.9e-4,4.1e-4],
        20: [6.9e-6,4.4e-4,5.9e-4,6.7e-4]
    }
}

# Set common axis labels and limits
xlabel = 'Layer Unit'
ylabel = 'Relative $L^2$ error'
ylim = [1e-5, 0]

# Create subplots
fig, axs = plt.subplots(nrows=1, ncols=3, sharex=True, sharey=True, figsize=(15, 5))

for i, network in enumerate(networks):
    for unit in units:
        if not np.isnan(values_ours[network][unit][0]):
            x = layers_units
            y = values_ours[network][unit]
            axs[i].plot(x, y, label=f"{network} - {unit} units")
            axs[i].plot(x, values_paper[network][unit], linestyle=':', label=f"{network} - {unit} units (paper)")

    # Set subplot title and legend
    axs[i].set_title(network)
    axs[i].legend()
    axs[i].set_yscale('log')

# Set axis labels and limits
fig.text(0.5, 0.04, xlabel, ha='center')
fig.text(0.04, 0.5, ylabel, va='center', rotation='vertical')
axs[0].set_ylim(ylim)

# Add scientific notation on y-axis
#plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))

# Show plot
plt.show()

