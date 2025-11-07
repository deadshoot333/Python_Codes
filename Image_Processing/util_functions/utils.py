import matplotlib.pyplot as plt

def show_image(image,title="Image",cmap_type="gray"):
    plt.imshow(image,cmap=cmap_type)
    plt.title(title)
    plt.axis("on")
    plt.show()

def plot_comparison(original,filtered,title_filtered):
    fig, (ax1, ax2) = plt.subplots(ncols=2,figsize=(8, 6),sharex=True,sharey=True)
    ax1.imshow(original, cmap=plt.cm.gray)
    ax1.set_title('original')
    ax1.axis('off')
    ax2.imshow(filtered, cmap=plt.cm.gray)
    ax2.set_title(title_filtered)
    ax2.axis('off')
    plt.show()