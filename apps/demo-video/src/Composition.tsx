import React from 'react';
import { Audio, Sequence, staticFile } from 'remotion';
import { Scene01Opener } from './scenes/Scene01Opener';
import { Scene02Problem } from './scenes/Scene02Problem';
import { Scene03Question } from './scenes/Scene03Question';
import { Scene04Architecture } from './scenes/Scene04Architecture';
import { Scene05Timeline } from './scenes/Scene05Timeline';
import { Scene06CaseA } from './scenes/Scene06CaseA';
import { Scene07CaseB } from './scenes/Scene07CaseB';
import { Scene08Metrics } from './scenes/Scene08Metrics';
import { Scene09Caveats } from './scenes/Scene09Caveats';
import { Scene10Outro } from './scenes/Scene10Outro';

/**
 * Total Audio Duration: ~116.64s @ 30fps = 3500 frames.
 * Exact Scene frame boundaries mapped to ElevenLabs speech silence intervals.
 */
export const MainVideo: React.FC = () => {
  return (
    <div style={{ flex: 1, display: 'flex', position: 'relative', width: '100%', height: '100%' }}>
      {/* Voice-over Audio Track */}
      <Audio src={staticFile('text-to-speech-fred.mp3')} />

      {/* 1. Opener (0 - 8s) */}
      <Sequence from={0} durationInFrames={240}>
        <Scene01Opener />
      </Sequence>

      {/* 2. El Problema (8s - 26s) */}
      <Sequence from={240} durationInFrames={540}>
        <Scene02Problem />
      </Sequence>

      {/* 3. La Pregunta (26s - 35.5s) */}
      <Sequence from={780} durationInFrames={285}>
        <Scene03Question />
      </Sequence>

      {/* 4. Arquitectura (35.5s - 48s) */}
      <Sequence from={1065} durationInFrames={375}>
        <Scene04Architecture />
      </Sequence>

      {/* 5. Timeline Replay (48s - 62s) */}
      <Sequence from={1440} durationInFrames={420}>
        <Scene05Timeline />
      </Sequence>

      {/* 6. Caso A (62s - 71s) */}
      <Sequence from={1860} durationInFrames={270}>
        <Scene06CaseA />
      </Sequence>

      {/* 7. Caso B Interceptado (71s - 93s) */}
      <Sequence from={2130} durationInFrames={660}>
        <Scene07CaseB />
      </Sequence>

      {/* 8. Métricas del Benchmark (93s - 106s) */}
      <Sequence from={2790} durationInFrames={390}>
        <Scene08Metrics />
      </Sequence>

      {/* 9. Caveats y Supuestos (106s - 111.5s) */}
      <Sequence from={3180} durationInFrames={165}>
        <Scene09Caveats />
      </Sequence>

      {/* 10. Outro (111.5s - 116.6s) */}
      <Sequence from={3345} durationInFrames={165}>
        <Scene10Outro />
      </Sequence>
    </div>
  );
};
