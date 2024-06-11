import matplotlib.pyplot as plt


def lineplot(data, title, x_label, y_label, set_ylim):
    """
    Function to create a simple line plot.
    """
    plt.figure(figsize=(14, 4))
    ax = data.plot(kind='line', linestyle='-', color='C0')

    # Customize the axes
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Set the title and labels
    plt.title(title)
    plt.xlabel(x_label, rotation=0)
    plt.ylabel(y_label)

    # Set y-axis limits
    ax.set_ylim(set_ylim)

    plt.show()


def barplot(data, title, x_label, y_label, width=0.8):
    """
    Function to create a simple bar plot.
    """
    plt.figure(figsize=(14, 4))
    ax = data.plot(kind='bar', width=width, color='C0')

    # Customize the axes
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Set the title and labels
    plt.title(title)
    plt.xlabel(x_label, rotation=0)
    plt.ylabel(y_label)

    # Ensure x-ticks are not rotated
    plt.xticks(rotation=0)

    plt.show()


def horizontal_bar_plot(data, title, x_label, y_label, axes=None, width=0.8):
    """
    Function to create a simple horizontal bar plot with reversed y-axis.
    """
    if axes is None:
        plt.figure(figsize=(14, 4))
        ax = plt.gca()
    else:
        ax = axes

    ax.barh(data.index, data.values, height=width, color='C0')

    # Set the title and labels
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    # Customize the axes
    ax.xaxis.tick_top()  # Move the x-axis to the top
    ax.xaxis.set_label_position('top')  # Move the x-axis label to the top
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    # Invert the y-axis
    ax.invert_yaxis()

    if axes is None:
        plt.show()


def histogram_plot(data, title, x_label, y_label, num_bins=10, xticks=None):
    """
    Function to create a simple histogram.
    """
    plt.figure(figsize=(14, 4))
    plt.hist(data, bins=num_bins, color='C0', edgecolor='black', linewidth=0.1)

    # Customize the axes
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)

    # Set the title and labels
    plt.title(title)
    plt.xlabel(x_label, rotation=0)
    plt.ylabel(y_label)

    # Set x-ticks if provided
    if xticks is not None:
        plt.xticks(xticks)

    plt.show()