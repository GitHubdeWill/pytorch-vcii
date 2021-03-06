"""
     resume and save model for training
"""
import torch

def resume(args, nets, index):
    """resume training
    
    Arguments:
        args {argparse} -- The arguments object specified in training_only_options
        nets {[nn.Module]} -- ['encoder', 'binarizer', 'decoder', 'unet'] for VCII network
        index {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """    
    names = ['encoder', 'binarizer', 'decoder', 'unet']

    for net_idx, net in enumerate(nets):
        if net is not None:
            name = names[net_idx]
            checkpoint_path = '{}/{}_{}_{:08d}.pth'.format(
                    args.model_dir, args.save_model_name, 
                    name, index)

            print('Loading %s from %s...' % (name, checkpoint_path))
            net.load_state_dict(torch.load(checkpoint_path))
    return nets

def save(args, nets, index, encoder):
    names = ['encoder', 'binarizer', 'decoder', 'unet']

    for net_idx, net in enumerate(nets):
        if net is not None:
            torch.save(net.state_dict(), 
                                 '{}/{}_{}_{:08d}.pth'.format(
                                     args.model_dir, args.save_model_name, 
                                     names[net_idx], index))