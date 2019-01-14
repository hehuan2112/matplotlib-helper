import os
import datetime
import argparse

import matplotlib as mpl
print('* loaded matplotlib', mpl.__version__)

import matplotlib.pyplot as plt

MAX_DAYS_ON_XAXIS = 63
DELTA_WEIGHT = 0.1

def draw_weight(title, ds, de, wh, wl, ws):
    img_path = './'
    figure_title = 'bw-%s-%s-%s' % (title, ds, de)
    fig_w = 29.7 / 2.54  # A4 size 
    fig_h = 21.0 / 2.54  # A4 size

    # prepare data
    wh = float(wh)
    wl = float(wl)
    dts = datetime.datetime.strptime(ds, '%Y-%m-%d')
    dte = datetime.datetime.strptime(de, '%Y-%m-%d')

    x_ticks = []
    x_ticklabels = []
    for d in range(MAX_DAYS_ON_XAXIS):
        day = dts + datetime.timedelta(days=d)
        x_ticks.append(d)
        x_ticklabels.append(day.strftime('%m-%d'))

        print('* add date %s' % day.strftime('%Y-%m-%d'))
        if day >= dte:
            break

    y_ticks = []
    y_ticklabels = []
    i = 0
    while True:
        w = wl + i*ws
        y_ticks.append(w)
        y_ticklabels.append('%.1f' % w)
        print('* add weight %s' % w)
        i += 1
        if w >= wh:
            break

    # draw 
    fig, axes = plt.subplots(1, 1, figsize=(fig_w, fig_h))
    ax = axes

    # config
    ax.set_title('Weight Record: %s' % title)
    ax.set_xlabel('Day')
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_ticklabels, rotation=90)

    ax.set_ylabel('Weight')
    ax.set_ylim([wl, wh])
    ax.set_yticks(y_ticks)
    ax.set_yticklabels(y_ticklabels)

    ax.grid()

    print('* drawn grid')
    # save figure
    if not os.path.exists(img_path): os.makedirs(img_path)
    img_fn = os.path.join(img_path, figure_title)
    fig.savefig(img_fn + '.pdf', bbox_inches='tight', pad_inches=0.02)

    print('* done!')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument("title", type=str, help="the low weight")
    parser.add_argument("weight_low", type=float, help="the low weight")
    parser.add_argument("weight_high", type=float, help="the high weight")
    parser.add_argument("-ws", "--weight_step", type=float, help="the delta weight drawn, default 0.1")
    parser.add_argument("-ds", "--date_start", help="the start date")
    parser.add_argument("-de", "--date_end", help="the end date")

    args = parser.parse_args()

    if args.weight_step == None:
        args.weight_step = DELTA_WEIGHT

    if args.date_start == None:
        args.date_start = datetime.datetime.now().strftime('%Y-%m-%d')
        args.date_end = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime('%Y-%m-%d')
    
    draw_weight(args.title, args.date_start, args.date_end, 
                args.weight_high, args.weight_low, args.weight_step)