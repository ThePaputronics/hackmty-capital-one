import React from 'react';
import { Composition, Still } from 'remotion';
import { MainVideo } from './Composition';
import { Thumbnail } from './scenes/Thumbnail';
import { ClassicalThumbnail } from './scenes/ClassicalThumbnail';
import { AestheticClassicalThumbnail } from './scenes/AestheticClassicalThumbnail';
import { AestheticClassicalThumbnailV2 } from './scenes/AestheticClassicalThumbnailV2';
import { ThumbnailRecolored } from './scenes/ThumbnailRecolored';

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="fred-demo"
        component={MainVideo}
        durationInFrames={3510}
        fps={30}
        width={1920}
        height={1080}
      />
      <Still
        id="thumbnail"
        component={Thumbnail}
        width={1920}
        height={1080}
      />
      <Still
        id="thumbnail-classical"
        component={ClassicalThumbnail}
        width={1920}
        height={1080}
      />
      <Still
        id="thumbnail-aesthetic"
        component={AestheticClassicalThumbnail}
        width={1920}
        height={1080}
      />
      <Still
        id="thumbnail-aesthetic-v2"
        component={AestheticClassicalThumbnailV2}
        width={1920}
        height={1080}
      />
      <Still
        id="thumbnail-recolored"
        component={ThumbnailRecolored}
        width={1920}
        height={1080}
      />
    </>
  );
};


